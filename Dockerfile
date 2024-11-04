FROM python:3.9-alpine

WORKDIR /srv

# tip 原由的镜像为简易容器，缺少很多常用工具，需要采用apk包管理器安装make工具
RUN apk update && apk add --no-cache make