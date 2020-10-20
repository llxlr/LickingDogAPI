#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from utils.log import LoggerV1
import argparse
import json
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

hometitle = os.getenv("HOMETITLE")  # 主页标题
title404 = os.getenv("TITLE404")  # 404页标题
docv = os.getenv("DOCV")  # doc版本
version = os.getenv("VERSION")  # api版本
description = "简单功能的个人实现 | 舔狗API 🍭"  # api描述
night = os.getenv("NIGHT")  # 夜间模式
port = os.getenv("PORT")  # 端口
start_time = os.getenv("START_TIME")  # 建站时间
domain = os.getenv("DOMAIN")  # 二级域名
sub, master, suffix = domain.split('.')
origin_regex = r'^https?\:\/\/([\a-zA-Z]+\.)?(127\.0\.0\.1|localhost|\.{}\.{})'.format(master, suffix)
cdn = os.getenv("CDN")
Copyright = {"author": "星旅人", "url": f"https://{master}.{suffix}/"}
analysis = json.loads(os.getenv("ANALYSIS"))
headers = json.loads(os.getenv("HEADER"))

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
    print(domain)
    pass
