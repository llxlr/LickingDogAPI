#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from utils.log import LoggerV1
import argparse
import os

path = os.path.dirname(__file__)
os.makedirs(f'{path}/cache/', exist_ok=True)
log = LoggerV1(os.path.join(f'{path}/cache/', 'info.log'))  # 设置一个日志记录器
loginfo = log.read_log()

parser = argparse.ArgumentParser()
parser.add_argument("-E", "--env", help="Custom PATH of dotenv file", action="store_true")
args = parser.parse_args()

if os.path.exists(f'{path}/.env') and not args.env:
    load_dotenv(verbose=True)
else:
    load_dotenv(dotenv_path=args.env, verbose=True)

hometitle = 'Licking Dog API'  # 主页标题
title404 = '404 Not Found'  # 404页标题
docv = '1.0.0'  # doc版本
version = '/v1'  # api版本
description = '简单功能的个人实现 | 舔狗API 🍭'  # api描述
night = 'on'  # 夜间模式
port = 8001  # 端口
start_time = 2019  # 建站时间
domain = 'api.white-album.top'  # 域名
sub, master, suffix = domain.split('.')
origin_regex = r'^https?\:\/\/([\a-zA-Z]+\.)?(127\.0\.0\.1|localhost|\.{}\.{})'.format(master, suffix)
cdn = 'https://cdn.jsdelivr.net/gh/llxlr/LickingDogAPI/data/'
Copyright = {"author": '星旅人', 'url': 'https://white-album.top/'}
analysis = {'google': 'UA-126485680-6', 'baidu': ''}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53'}

# Admin
Username = os.getenv("Username")
Password = os.getenv("Password")
# Baidu AI API
Baidu_APP_ID = os.getenv("APP_ID")
Baidu_API_KEY = os.getenv("API_KEY")
Baidu_SECRET_KEY = os.getenv("SECRET_KEY")
# Bilibili
sessdata = os.getenv("sessdata")
bili_jct = os.getenv("bili_jct")
# CloudFlare
cf_zone_id = os.getenv("cf_zone_id")
cf_user_id = os.getenv("cf_user_id")
cf_token = os.getenv("cf_token")
cf_email = os.getenv("cf_email")
cf_global_api_key = os.getenv("cf_global_api_key")
# Email
email = os.getenv("username")
password = os.getenv("password")
# Github
github_token = os.getenv("TOKEN")
# Pixiv
PIXIV_EMAIL = os.getenv("PIXIV_EMAIL")
PIXIV_PASSWD = os.getenv("PIXIV_PASSWD")
# RSA
public_key = os.getenv("public_key")
private_key = os.getenv("private_key")
# Server
sckey = os.getenv("SCKEY")


if __name__ == "__main__":
    pass
