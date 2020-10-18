FROM python:3.7-slim-buster
LABEL maintainer="James Yang <i@white-album.top>"

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN rm -rf ./{.env,.env.example,.gitattributes,.gitignore,deploy.sh,docker-compose.yml,Dockerfile,LICENSE,README.md} && \
    rm -rf ./{.git,.github,.idea,.vscode,cache,conf,data,venv} && \
    find . -path ./venv -prune -o -type d -name "__pycache__" | grep "__pycache__" | xargs rm -rf && \
    apt-get update -y && apt-get upgrade -y && \
    apt-get install g++ gcc make build-essential libc-dev musl-dev libxslt-dev apt-utils -y && \
    pip3 install --upgrade pip --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip3 install -r requirements.txt --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    apt-get autoremove g++ gcc make build-essential libc-dev musl-dev libxslt-dev apt-utils -y && \
    apt-get clean && rm -rf requirements.txt && rm -rf /tmp/* && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' > /etc/timezone

#EXPOSE 8001

CMD ["python", "manage.py"]
#CMD ["uvicorn", "manage:app", "--host", "127.0.0.1", "--port", "8001"]
#CMD ["gunicorn", "manage:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]
