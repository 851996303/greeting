FROM python:3.9-alpine

WORKDIR /srv

# 采用apk包管理器安装make工具
RUN apk update && apk add --no-cache make