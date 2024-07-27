#!/bin/sh

curl -L -o gitea-api.yaml https://docs.gitea.com/redocusaurus/plugin-redoc-1.yaml

swagger-codegen generate \
  -i gitea-api.yaml \
  -l python \
  -o . \
  -DpackageName=gitea_client
