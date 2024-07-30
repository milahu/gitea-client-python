#!/bin/sh

# NOTE usually we would use https://gitea.your.host/swagger.v1.json
# to generate an API client with only the enabled API methods
#
# but here we use the generic gitea API spec to enable all API methods
# so when some API methods are disabled on a specific gitea host
# then these API methods will fail with HTTP 404
#
# see also
# https://gitea.com/gitea/docs/src/branch/main/docs/development/api-usage.md#api-guide

# API specs url from "Download OpenAPI specification" at
# https://docs.gitea.com/api/1.22/

curl -L -o gitea-api.yaml https://docs.gitea.com/redocusaurus/plugin-redoc-1.yaml

swagger-codegen generate \
  -i gitea-api.yaml \
  -l python \
  -o . \
  -DpackageName=gitea_client
