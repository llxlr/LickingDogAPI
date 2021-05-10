FROM python:3.8-slim-buster
LABEL maintainer="James Yang <i@xhlr.top>"

COPY . /app

WORKDIR /app

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install g++ gcc make build-essential libc-dev musl-dev libxslt-dev apt-utils -y && \
    pip3 install --upgrade pip --no-cache-dir -i https://opentuna.cn/pypi/web/simple && \
    pip3 install -r requirements.txt --no-cache-dir -i https://opentuna.cn/pypi/web/simple && \
    apt-get autoremove g++ gcc make build-essential libc-dev musl-dev libxslt-dev apt-utils -y && \
    apt-get clean && rm -rf requirements.txt && rm -rf /tmp/*

ENV HOST 0.0.0.0
ENV PORT 8001

EXPOSE 8001

CMD ["python", "manage.py"]
