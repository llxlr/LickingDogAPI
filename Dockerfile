FROM python:3.8-slim-buster
LABEL maintainer="llxlr <i@xhlr.top>"

COPY . /

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install g++ gcc make build-essential libc-dev musl-dev libxslt-dev apt-utils -y && \
    pip3 install --upgrade pip poetry --no-cache-dir -i https://mirrors.bfsu.edu.cn/pypi/web/simple && \
    poetry config virtualenvs.create false && poetry install && \
    apt-get autoremove g++ gcc make build-essential libc-dev musl-dev libxslt-dev apt-utils -y && \
    apt-get clean && rm -rf /tmp/* ~/.poetry

EXPOSE 8001

ENTRYPOINT ["python", "main.py"]
