#!/usr/bin/env python3

# fetch notifications from gitea, store them on disk



# related ...

# https://github.com/go-gitea/gitea/issues/13697
# [API] Add Activity Feed endpoints

# https://github.com/MichaelMure/git-bug/pull/1077
# WIP: Gitea/Forgejo bridge



import os
import re
import sys
import json
import logging
import urllib.parse

# https://github.com/milahu/gitea-client-python
#sys.path.insert(0, "gitea-client-python")
import gitea_client

import urllib3



# example remotes.json

# note: token must be generated in gitea > settings > applications
# with read-write access to notifications
# with read access to issues and pull requests

"""
{
  "darktea.onion": {
    "url": "http://it7otdanqu7ktntxzm427cba6i53w6wlanlh23v5i3siqmos47pzhvyd.onion/",
    "token": "xxxxxxxx",
    "proxy": "socks5h://127.0.0.1:9050"
  }
}
"""

remotes_path = os.path.expanduser("~/.config/gitea-client/remotes.json")

cache_path = os.path.expanduser("~/.cache/gitea-client/remotes")



def main():

    logging_level = "DEBUG"
    logging_level = "INFO"
    #logging_level = "ERROR"

    logging.basicConfig(
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        level=logging_level,
    )

    logger = logging.getLogger(__name__)

    # hide retry warnings
    logging.getLogger("urllib3.connectionpool").setLevel("ERROR")

    with open(remotes_path) as f:
        remotes = json.load(f)

    for remote_name, remote in remotes.items():
        remote["name"] = remote_name

    for remote in remotes.values():

        if remote.get("enabled") == False:
            continue

        try:
            client = GiteaClient(remote)
        except Exception as exc:
            print(remote["name"] + f": error: {type(exc).__name__}: {str(exc)}")
            continue

        print(remote["name"] + ": info: fetching notifications")
        try:
            for note in client.fetch_notifications(mark_as_read=False):
                # write notification to disk
                path = urllib.parse.urlparse(note.subject.html_url).path[1:]
                path = os.path.join(cache_path, remote["name"], path)
                print("writing", path)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                # note: this replaces existing files
                with open(path, "w") as f:
                    f.write("\n\n".join([
                        note.subject.html_url,
                        note.subject.title,
                        note.subject.body,
                    ]) + "\n")
                client.mark_notification_as_read(note.id)
        except urllib3.exceptions.MaxRetryError as exc:
            print(remote["name"] + ": error: remote is not reachable")



class GiteaClient:

    def __init__(self, remote):

        self.config = gitea_client.configuration.Configuration()

        self.config.host = urllib.parse.urljoin(remote["url"], "/api/v1")

        assert self.is_valid_token(remote["token"]), "invalid token: " + repr(remote["token"])

        self.config.api_key["token"] = remote["token"]

        #self.config.debug = True

        # socks proxy support requires patching of generated code
        # https://github.com/swagger-api/swagger-codegen/issues/8702
        # https://github.com/milahu/gitea-client-python/issues/1
        if proxy := remote.get("proxy"):
            self.config.proxy = proxy

        self.client = gitea_client.api_client.ApiClient(self.config)

    def is_valid_token(self, token):
        return re.fullmatch("[0-9a-f]{40}", token) != None

    def get_version(self):
        "get the gitea version"
        return gitea_client.MiscellaneousApi(self.client).get_version().version

    def get_current_user(self):
        "get the logged in user, aka the token owner"
        return gitea_client.UserApi(self.client).user_get_current()
        # user_id = current_user.id

    def fetch_notifications(self, mark_as_read=False):

        note_list = gitea_client.NotificationApi(self.client).notify_get_list()

        for note in note_list:

            url = note.subject.html_url
            owner = note.repository.owner.login
            repo = note.repository.name
            title = note.subject.title

            # fetch body
            body = None

            if note.subject.type == "Issue":
                issue_id = int(note.subject.url.split("/")[-1])
                issue = gitea_client.IssueApi(self.client).issue_get_issue(owner, repo, issue_id)
                # TODO get issue comments
                # GET /repos/{owner}/{repo}/issues/{index}/comments # List all comments on an issue
                # GET /repos/{owner}/{repo}/issues/comments/{id}/reactions # Get a list of reactions from a comment of an issue
                # GET /repos/{owner}/{repo}/issues/{index}/timeline # List all comments and events on an issue
                note.subject.issue = issue
                note.subject.body = issue.body

            elif note.subject.type == "Pull":
                pull_id = int(note.subject.url.split("/")[-1])
                pull_request = gitea_client.RepositoryApi(self.client).repo_get_pull_request(owner, repo, pull_id)
                # TODO get pull_request comments
                # GET /repos/{owner}/{repo}/pulls/{index}/reviews # List all reviews for a pull request
                # GET /repos/{owner}/{repo}/pulls/{index}/reviews/{id} # Get a specific review for a pull request
                # GET /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments # Get a specific review for a pull request
                note.subject.pull_request = pull_request
                note.subject.body = pull_request.body

            else:
                print("FIXME handle note.subject.type", note.subject.type)

            # FIXME comments are not returned by NotificationApi
            # but new comments are listed in the home page feed of gitea
            # https://github.com/go-gitea/gitea/issues/13697
            # [API] Add Activity Feed endpoints

            if mark_as_read:
                self.mark_notification_as_read(note.id)

            yield note

    def mark_notification_as_read(self, note_id):
        "mark notification as read"
        # do this in a separate API call for command-query separation
        # https://en.wikipedia.org/wiki/Command%E2%80%93query_separation
        # because fetching and storing of notifications can fail
        # and then we dont want the notifications to be marked as "read"
        gitea_client.NotificationApi(self.client).notify_read_thread(note_id)



if __name__ == "__main__":

    main()
