# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: {{AppVer | JSEscape}}
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gitea_client.api_client import ApiClient


class NotificationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def notify_get_list(self, **kwargs):  # noqa: E501
        """List users's notification threads  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_get_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool all: If true, show notifications marked as read. Default value is false
        :param list[str] status_types: Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned.
        :param list[str] subject_type: filter notifications by subject type
        :param datetime since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
        :param datetime before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
        :param int page: page number of results to return (1-based)
        :param int limit: page size of results
        :return: list[NotificationThread]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.notify_get_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.notify_get_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def notify_get_list_with_http_info(self, **kwargs):  # noqa: E501
        """List users's notification threads  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_get_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool all: If true, show notifications marked as read. Default value is false
        :param list[str] status_types: Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned.
        :param list[str] subject_type: filter notifications by subject type
        :param datetime since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
        :param datetime before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
        :param int page: page number of results to return (1-based)
        :param int limit: page size of results
        :return: list[NotificationThread]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['all', 'status_types', 'subject_type', 'since', 'before', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method notify_get_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'all' in params:
            query_params.append(('all', params['all']))  # noqa: E501
        if 'status_types' in params:
            query_params.append(('status-types', params['status_types']))  # noqa: E501
            collection_formats['status-types'] = 'multi'  # noqa: E501
        if 'subject_type' in params:
            query_params.append(('subject-type', params['subject_type']))  # noqa: E501
            collection_formats['subject-type'] = 'multi'  # noqa: E501
        if 'since' in params:
            query_params.append(('since', params['since']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/notifications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NotificationThread]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def notify_get_repo_list(self, owner, repo, **kwargs):  # noqa: E501
        """List users's notification threads on a specific repo  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_get_repo_list(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the repo (required)
        :param str repo: name of the repo (required)
        :param bool all: If true, show notifications marked as read. Default value is false
        :param list[str] status_types: Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned
        :param list[str] subject_type: filter notifications by subject type
        :param datetime since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
        :param datetime before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
        :param int page: page number of results to return (1-based)
        :param int limit: page size of results
        :return: list[NotificationThread]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.notify_get_repo_list_with_http_info(owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.notify_get_repo_list_with_http_info(owner, repo, **kwargs)  # noqa: E501
            return data

    def notify_get_repo_list_with_http_info(self, owner, repo, **kwargs):  # noqa: E501
        """List users's notification threads on a specific repo  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_get_repo_list_with_http_info(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the repo (required)
        :param str repo: name of the repo (required)
        :param bool all: If true, show notifications marked as read. Default value is false
        :param list[str] status_types: Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned
        :param list[str] subject_type: filter notifications by subject type
        :param datetime since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
        :param datetime before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
        :param int page: page number of results to return (1-based)
        :param int limit: page size of results
        :return: list[NotificationThread]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'all', 'status_types', 'subject_type', 'since', 'before', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method notify_get_repo_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in params or
                                                       params['owner'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `owner` when calling `notify_get_repo_list`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if self.api_client.client_side_validation and ('repo' not in params or
                                                       params['repo'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repo` when calling `notify_get_repo_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []
        if 'all' in params:
            query_params.append(('all', params['all']))  # noqa: E501
        if 'status_types' in params:
            query_params.append(('status-types', params['status_types']))  # noqa: E501
            collection_formats['status-types'] = 'multi'  # noqa: E501
        if 'subject_type' in params:
            query_params.append(('subject-type', params['subject_type']))  # noqa: E501
            collection_formats['subject-type'] = 'multi'  # noqa: E501
        if 'since' in params:
            query_params.append(('since', params['since']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repo}/notifications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NotificationThread]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def notify_get_thread(self, id, **kwargs):  # noqa: E501
        """Get notification thread by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_get_thread(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id of notification thread (required)
        :return: NotificationThread
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.notify_get_thread_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.notify_get_thread_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def notify_get_thread_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get notification thread by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_get_thread_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id of notification thread (required)
        :return: NotificationThread
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method notify_get_thread" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `notify_get_thread`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/notifications/threads/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotificationThread',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def notify_new_available(self, **kwargs):  # noqa: E501
        """Check if unread notifications exist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_new_available(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NotificationCount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.notify_new_available_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.notify_new_available_with_http_info(**kwargs)  # noqa: E501
            return data

    def notify_new_available_with_http_info(self, **kwargs):  # noqa: E501
        """Check if unread notifications exist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_new_available_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NotificationCount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method notify_new_available" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/notifications/new', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotificationCount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def notify_read_list(self, **kwargs):  # noqa: E501
        """Mark notification threads as read, pinned or unread  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_read_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime last_read_at: Describes the last point that notifications were checked. Anything updated since this time will not be updated.
        :param str all: If true, mark all notifications on this repo. Default value is false
        :param list[str] status_types: Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.
        :param str to_status: Status to mark notifications as, Defaults to read.
        :return: list[NotificationThread]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.notify_read_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.notify_read_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def notify_read_list_with_http_info(self, **kwargs):  # noqa: E501
        """Mark notification threads as read, pinned or unread  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_read_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime last_read_at: Describes the last point that notifications were checked. Anything updated since this time will not be updated.
        :param str all: If true, mark all notifications on this repo. Default value is false
        :param list[str] status_types: Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.
        :param str to_status: Status to mark notifications as, Defaults to read.
        :return: list[NotificationThread]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['last_read_at', 'all', 'status_types', 'to_status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method notify_read_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'last_read_at' in params:
            query_params.append(('last_read_at', params['last_read_at']))  # noqa: E501
        if 'all' in params:
            query_params.append(('all', params['all']))  # noqa: E501
        if 'status_types' in params:
            query_params.append(('status-types', params['status_types']))  # noqa: E501
            collection_formats['status-types'] = 'multi'  # noqa: E501
        if 'to_status' in params:
            query_params.append(('to-status', params['to_status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/notifications', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NotificationThread]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def notify_read_repo_list(self, owner, repo, **kwargs):  # noqa: E501
        """Mark notification threads as read, pinned or unread on a specific repo  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_read_repo_list(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the repo (required)
        :param str repo: name of the repo (required)
        :param str all: If true, mark all notifications on this repo. Default value is false
        :param list[str] status_types: Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.
        :param str to_status: Status to mark notifications as. Defaults to read.
        :param datetime last_read_at: Describes the last point that notifications were checked. Anything updated since this time will not be updated.
        :return: list[NotificationThread]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.notify_read_repo_list_with_http_info(owner, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.notify_read_repo_list_with_http_info(owner, repo, **kwargs)  # noqa: E501
            return data

    def notify_read_repo_list_with_http_info(self, owner, repo, **kwargs):  # noqa: E501
        """Mark notification threads as read, pinned or unread on a specific repo  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_read_repo_list_with_http_info(owner, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the repo (required)
        :param str repo: name of the repo (required)
        :param str all: If true, mark all notifications on this repo. Default value is false
        :param list[str] status_types: Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.
        :param str to_status: Status to mark notifications as. Defaults to read.
        :param datetime last_read_at: Describes the last point that notifications were checked. Anything updated since this time will not be updated.
        :return: list[NotificationThread]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'all', 'status_types', 'to_status', 'last_read_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method notify_read_repo_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in params or
                                                       params['owner'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `owner` when calling `notify_read_repo_list`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if self.api_client.client_side_validation and ('repo' not in params or
                                                       params['repo'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repo` when calling `notify_read_repo_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []
        if 'all' in params:
            query_params.append(('all', params['all']))  # noqa: E501
        if 'status_types' in params:
            query_params.append(('status-types', params['status_types']))  # noqa: E501
            collection_formats['status-types'] = 'multi'  # noqa: E501
        if 'to_status' in params:
            query_params.append(('to-status', params['to_status']))  # noqa: E501
        if 'last_read_at' in params:
            query_params.append(('last_read_at', params['last_read_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repo}/notifications', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NotificationThread]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def notify_read_thread(self, id, **kwargs):  # noqa: E501
        """Mark notification thread as read by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_read_thread(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id of notification thread (required)
        :param str to_status: Status to mark notifications as
        :return: NotificationThread
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.notify_read_thread_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.notify_read_thread_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def notify_read_thread_with_http_info(self, id, **kwargs):  # noqa: E501
        """Mark notification thread as read by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.notify_read_thread_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id of notification thread (required)
        :param str to_status: Status to mark notifications as
        :return: NotificationThread
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'to_status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method notify_read_thread" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `notify_read_thread`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'to_status' in params:
            query_params.append(('to-status', params['to_status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/notifications/threads/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotificationThread',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
