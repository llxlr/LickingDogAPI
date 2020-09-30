<p align="center">
  <a href="https://api.white-album.top/">
    <img width="200px" src="https://cdn.jsdelivr.net/gh/llxlr/LickingDogAPI/static/img/mur_cat.png" alt='LickingDogAPI'>
  </a>
  <br>
  <a href="https://github.com/llxlr/LickingDogAPI/actions">
    <img src="https://github.com/llxlr/LickingDogAPI/workflows/Check%20Python%20Syntax/badge.svg" alt="Check Python Syntax">
  </a>
  <a href="https://github.com/llxlr/LickingDogAPI/actions">
    <img src="https://github.com/llxlr/LickingDogAPI/workflows/CodeQL/badge.svg" alt="CodeQL">
  </a>
  <a href="https://github.com/llxlr/LickingDogAPI/actions">
    <img src="https://github.com/llxlr/LickingDogAPI/workflows/Auto%20Deploy/badge.svg" alt="Auto Deploy">
  </a>
  <a href="https://github.com/llxlr/LickingDogAPI/actions">
    <img src="https://github.com/llxlr/LickingDogAPI/workflows/Merge%20Imgbot/badge.svg" alt="Merge Imgbot">
  </a>
  <br>
  <em>Licking Dog API | 舔狗API 🍭 - Made <span style="color:#F03D41">❤</span> by james yang & Power by <a src="https://fastapi.tiangolo.com/">FastAPI</a></em>
</p>
<blockquote><p align="center">敬我暗恋的人</p></blockquote>

# 项目还在发育~~间歇性瞎写~~，处于不断迭代状态

# 使用

```bash
$ git clone https://github.com/llxlr/LickingDogAPI.git
$ cd LickingDogAPI
$ python -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
$ uvicorn wsgi:app --host 127.0.0.1 --port 8001
```


## 用作 Systemd 服务

编辑`/etc/systemd/system/ldapi.service`：

```bash
$ sudo nano /etc/systemd/system/ldapi.service
```

加入以下内容：

```txt
[Unit]
Description=LickingDogAPI with Uvicorn
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/www/html/LickingDogAPI
Environment="PATH=/www/html/LickingDogAPI/venv/bin"
ExecStart=/www/html/LickingDogAPI/venv/bin/uvicorn wsgi:app --host 127.0.0.1 --port 8001
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true
Restart=always
RestartSec=5
StartLimitInterval=0

[Install]
WantedBy=multi-user.target
```

或者使用`gunicorn`（注：gunicorn仅支持Linux系统）:
将`uvicorn wsgi:app --host 127.0.0.1 --port 8001`
替换为`gunicorn -b 127.0.0.1:8001 -k uvicorn.workers.UvicornWorker wsgi:app`

有以下命令：

```bash
$ sudo systemctl daemon-reload  # 重载所有修改过的配置文件
$ sudo systemctl enable ldapi  # 设置自动启动
$ sudo systemctl start ldapi  # 启动服务
$ sudo systemctl stop ldapi  # 停止服务
$ sudo systemctl restart ldapi  # 重启服务
$ sudo systemctl status ldapi  # 查看服务状态
```

## ~~Docker 部署~~

还没搞明白

```bash
$ sudo docker run -d -p 4444:4444 --shm-size=2g  -e TZ=Asia/Shanghai selenium/standalone-chrome

$ sudo mkdir /etc/api/ && sudo cp .env /etc/api/.env
$ sudo docker build . -t llxlr/licking-dog-api:v0.0.1
$ sudo docker run --rm -p 8001:8001 -v /etc/api/.env:/.env -t llxlr/licking-dog-api:v0.0.1 #临时调试
$ sudo docker run -d -p 8001:8001 -v /etc/api/.env:/.env -t llxlr/licking-dog-api:v0.0.1   #或直接部署

$ sudo docker save -o ./licking-dog-api-v0.0.1.tar llxlr/licking-dog-api:v0.0.1 #导出镜像
$ sudo docker load --input ./licking-dog-api-v0.0.1.tar #导入镜像
$ sudo docker export licking-dog-api-v0.0.1 > ./licking-dog-api-v0.0.1.tar #导出容器
$ sudo docker import ./licking-dog-api-v0.0.1.tar licking-dog-api-v0.0.1 #导入容器
```

# 文档

交互文档: [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)

``` 
POST:   发送数据
GET:    请求数据
PUT:    更新数据
DELETE: 删除数据
```

# 参考链接

[FastAPI](https://fastapi.tiangolo.com/)

[Starlette](https://www.starlette.io/)

[Uvicorn](https://www.uvicorn.org/)
