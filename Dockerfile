FROM python:3.7-slim-buster

LABEL maintainer="James Yang <i@white-album.top>"

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN rm -rf ./{.env,.env.example,.gitattributes,.gitignore,deploy.sh,docker-compose.yml,Dockerfile,LICENSE,README.md} && \
    rm -rf ./{.git,.github,.idea,.vscode,cache,conf,data,venv,__pycache__} && \
    rm -rf ./{router/__pycache__,router/api/__pycache__,} && \
    rm -rf ./{items/__pycache__,items/anime/__pycache__,items/ml/__pycache__,items/ml/yolo/__pycache__,items/ml/catvsdog/__pycache__} && \
    rm -rf ./{utils/__pycache__,utils/auth/__pycache__,utils/lib/__pycache__,utils/sql/__pycache__} && \
    apt-get update -y && apt-get upgrade -y && \
    apt-get install g++ gcc make build-essential libc-dev musl-dev libxslt-dev apt-utils -y && \
    pip3 install --upgrade pip --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip3 install -r requirements.txt --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    apt-get autoremove g++ gcc make build-essential libc-dev musl-dev libxslt-dev apt-utils -y && \
    apt-get clean && rm -rf requirements.txt && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' > /etc/timezone

EXPOSE 8001

#CMD [""]

CMD ["uvicorn", "wsgi:app", "--host", "127.0.0.1", "--port", "8001"]
