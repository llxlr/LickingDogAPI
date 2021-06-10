FROM python:3.8-slim-buster
LABEL maintainer="James Yang <i@xhlr.top>"

COPY ./app /app

WORKDIR /app

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install g++ gcc make build-essential libc-dev musl-dev libxslt-dev apt-utils -y && \
    pip3 install --upgrade pip poetry==1.2.0a1 --no-cache-dir -i https://mirrors.bfsu.edu.cn/pypi/web/simple && \
    poetry config virtualenvs.create true && poetry install && \
    apt-get autoremove g++ gcc make build-essential libc-dev musl-dev libxslt-dev apt-utils -y && \
    apt-get clean && rm -rf /tmp/* ~/.poetry

ENV HOST 0.0.0.0
ENV PORT 8001

EXPOSE 8001

ENTRYPOINT ["python", "manage.py"]
