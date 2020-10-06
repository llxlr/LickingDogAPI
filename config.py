from dotenv import load_dotenv
from utils.log import Logger
import os

hometitle = "Licking Dog API"  # 主页标题
title404 = "404 Not Found"  # 404页标题
domain = "api.white-album.top"  # 域名
port = 8001  # 端口
docv = "1.0.0"  # doc版本
version = "/v1"  # api版本
description = "简单功能的个人实现 | 舔狗API 🍭"  # api 描述
start_time = 2019  # 建站时间
Copyright = {"author": "星旅人", "url": "https://white-album.top/"}
analysis = {'google': 'UA-126485680-6', 'baidu': ''}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53'}
domain = domain.split('.')
origins = [
    f"http://{domain[1]}.{domain[2]}", f"https://{domain[1]}.{domain[2]}",
    "http://127.0.0.1", f"http://127.0.0.1:{port}", "https://127.0.0.1", f"https://127.0.0.1:{port}",
    "http://localhost", f"http://localhost:{port}", "https://localhost", f"https://localhost:{port}",
]
origin_regex = r'^https?\:\/\/([\a-zA-Z]+\.)?(127\.0\.0\.1|localhost|\.{}\.{})'.format(domain[1], domain[2])
cdn = 'https://cdn.jsdelivr.net/gh/llxlr/LickingDogAPI/data/'

path = f'{os.path.dirname(__file__)}/cache/'
os.makedirs(path, exist_ok=True)
log = Logger(os.path.join(path, 'info.log'))  # 设置一个日志记录器

load_dotenv(verbose=True)
Username, Password = map(os.getenv, ["Username", "Password"])  # Admin
Baidu_APP_ID, Baidu_API_KEY, Baidu_SECRET_KEY = map(os.getenv, ["APP_ID", "API_KEY", "SECRET_KEY"])  # Baidu AI API
sessdata, bili_jct = map(os.getenv, ["sessdata", "bili_jct"])  # Bilibili
cf_zone_id, cf_user_id, cf_token, cf_email, cf_global_api_key = map(os.getenv, [
    "cf_zone_id", "cf_user_id", "cf_token", "cf_email", "cf_auth_key"])  # CloudFlare
email, password = map(os.getenv, ["username", "password"])   # Email
github_token = os.getenv("TOKEN")  # Github
PIXIV_EMAIL, PIXIV_PASSWD = map(os.getenv, ["PIXIV_EMAIL", "PIXIV_PASSWD"])  # Pixiv
public_key, private_key = map(os.getenv, ["public_key", "private_key"])  # RSA
sckey = os.getenv("SCKEY")  # Server


if __name__ == "__main__":
    print(private_key)
