#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from fake_useragent import UserAgent
from utils.log import LoggerV1
import data
import json
import os

path = os.path.dirname(__file__)
os.makedirs(f'{path}/cache/', exist_ok=True)

log = LoggerV1(os.path.join(f'{path}/cache/', 'info.log'))  # 设置一个日志记录器
loginfo = log.read_log()

ua = UserAgent(path=data.fake_useragent())
headers = {'User-Agent': ua.random}

with open(f'{path}/config.json', 'r', encoding='utf-8') as f:
    SETUP = json.loads(f.read())

if os.path.exists(f'{path}/../.env'):
    load_dotenv(dotenv_path=f'{path}/../.env', verbose=True)
else:
    load_dotenv(dotenv_path='/etc/api/.env', verbose=True)

title = SETUP['TITLE']  # 主页标题
version = SETUP['VERSION']  # api版本
api_version = '/v1'
api_test_version = '/v2'
description = SETUP['DESCRIPTION']  # api描述
start_time = SETUP['START_TIME']  # 建站时间
cdn = SETUP['CDN']
Copyright = SETUP['COPYRIGHT']
domain = SETUP['DOMAIN']  # 二级域名
sub, master, suffix = domain.split('.')
origin_regex = r'^https?\:\/\/([\a-zA-Z]+\.)?(127\.0\.0\.1|localhost|\.{}\.{})'.format(master, suffix)

# Admin
Username = os.getenv('Username')
Password = os.getenv('Password')
# ANALYSIS
analysis = {
    'google': os.getenv('GOOGLE_ANALYSIS'),
    'baidu': os.getenv('BAIDU_FENXI'),
}
# Baidu AI API
Baidu_APP_ID = os.getenv('APP_ID')
Baidu_API_KEY = os.getenv('API_KEY')
Baidu_SECRET_KEY = os.getenv('SECRET_KEY')
# Bilibili
sessdata = os.getenv('sessdata')
bili_jct = os.getenv('bili_jct')
# CloudFlare
cf_zone_id = os.getenv('cf_zone_id')
cf_user_id = os.getenv('cf_user_id')
cf_token = os.getenv('cf_token')
cf_email = os.getenv('cf_email')
cf_global_api_key = os.getenv('cf_global_api_key')
# Email
email = os.getenv('username')
password = os.getenv('password')
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
PIXIV_EMAIL = os.getenv('PIXIV_EMAIL')
PIXIV_PASSWD = os.getenv('PIXIV_PASSWD')
# RSA
public_key = os.getenv('public_key')
private_key = os.getenv('private_key')
# Server
sckey = os.getenv('SCKEY')


if __name__ == "__main__":
    print(port)
    pass
