#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv
from fake_useragent import UserAgent

from utils.log import LoggerV1
import data

path = os.path.dirname(__file__)
os.makedirs(f'{path}/cache/', exist_ok=True)
# 设置一个日志记录器
log = LoggerV1(os.path.join(f'{path}/cache/', 'info.log'))
log_info = log.read_log()
# 用户代理
ua = UserAgent(path=data.fake_useragent())
headers = {'User-Agent': ua.random}

if os.path.exists(f'{path}/.env'):
    load_dotenv(verbose=True)
else:
    load_dotenv(dotenv_path='/etc/api/.env', verbose=True)

title = os.getenv('TITLE')  # 主页标题
version = os.getenv('VERSION')  # api版本
api_version = '/v1'
api_test_version = '/v2'
description = os.getenv('DESCRIPTION')  # api描述
start_time = os.getenv('START_TIME')  # 建站时间
cdn = os.getenv('CDN')
Copyright = {"author": os.getenv('AUTHOR'), "url": os.getenv('URL')}
domain = f"api.{os.getenv('DOMAIN')}"  # 二级域名
sub, master, suffix = domain.split('.')
origin_regex = r'^https?\:\/\/([\a-zA-Z]+\.)?(127\.0\.0\.1|localhost|\.{}\.{})'.format(master, suffix)

HOST, PORT = os.getenv('HOST', '0.0.0.0'), os.getenv('PORT', 8001)
# Admin
Username, Password = os.getenv('USERNAME'), os.getenv('PASSWORD')
# Email
email, email_password = os.getenv('email'), os.getenv('email_password')
# ANALYSIS
analysis = {
    'google': os.getenv('GOOGLE_ANALYSIS'),
    'baidu': os.getenv('BAIDU_FENXI'),
}
# Baidu AI API
Baidu_APP_ID, Baidu_API_KEY, Baidu_SECRET_KEY = os.getenv('APP_ID'), os.getenv('API_KEY'), os.getenv('SECRET_KEY')
# Bilibili
sessdata, bili_jct, buvid3 = os.getenv('sessdata'), os.getenv('bili_jct'), os.getenv('buvid3')
# CloudFlare
cf_zone_id = os.getenv('cf_zone_id')
cf_user_id = os.getenv('cf_user_id')
cf_token = os.getenv('cf_token')
cf_email = os.getenv('cf_email')
cf_global_api_key = os.getenv('cf_global_api_key')
# Github
github_token = os.getenv('TOKEN')
# Gitalk
gitalk_config = {
    'clientID': os.getenv('gitalk_clientID'),
    'clientSecret': os.getenv('gitalk_clientSecret'),
    'repo': os.getenv('gitalk_repo'),
    'owner': os.getenv('gitalk_owner'),
    'admin': os.getenv('gitalk_admin'),
}
# Pixiv
PIXIV_USERNAME = os.getenv('PIXIV_USERNAME')
PIXIV_PASSWD = os.getenv('PIXIV_PASSWD')
PIXIV_REFRESH_TOKEN = os.getenv('PIXIV_REFRESH_TOKEN')
# RSA
public_key, private_key = os.getenv('public_key'), os.getenv('private_key')  # RSA
# Server Chen Turbo
sckey = os.getenv('SCKEY')


if __name__ == "__main__":
    # TODO:
    pass
