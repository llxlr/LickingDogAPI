from dotenv import load_dotenv
import os

hometitle = "Licking Dog API"  # 主页标题
title404 = "404 Not Found"  # 404页标题
domain = "api.white-album.top"  # 域名
port = 8001  # 端口
docv = "1.0.0"  # doc版本
version = "/v" + docv[0]  # api版本
description = "简单功能的个人实现 | 舔狗API 🍭"  # api 描述
start_time = 2019  # 建站时间
Copyright = {"author": "星旅人", "url": "https://white-album.top/"}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53'}
load_dotenv(verbose=True)
Username, Password = map(os.getenv, ["Username", "Password"])
PIXIV_EMAIL, PIXIV_PASSWD = map(os.getenv, ["PIXIV_EMAIL", "PIXIV_PASSWD"])  # Pixiv
cf_zone_id, cf_email, cf_auth_key = map(os.getenv, ["cf_zone_id", "cf_email", "cf_auth_key"])  # CloudFlare
Baidu_APP_ID, Baidu_API_KEY, Baidu_SECRET_KEY = map(os.getenv, ["APP_ID", "API_KEY", "SECRET_KEY"])  # Baidu AI API
public_key, private_key = map(lambda x: os.getenv(x).strip(), ["public_key", "private_key"])
github_token = list(map(os.getenv, ["TOKEN"]))

if __name__ == "__main__":
    print(private_key)
