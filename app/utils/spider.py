#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests.exceptions import ConnectionError, ConnectTimeout
import requests
import config


def get(url, params=None, headers: dict = None):
    headers = config.headers if not headers else None
    response = requests.get(url=url, params=params, headers=headers)
    try:
        if response.status_code == 200:
            response.encoding = 'utf-8'
        return response
    except:
        return False


def post(url, data=None, json=None, headers: dict = None):
    headers = config.headers if not headers else None
    response = requests.post(url=url, data=data, json=json, headers=headers)
    try:
        if response.status_code == 200:
            response.encoding = 'utf-8'
        return response
    except:
        return False


def put(url, data=None, headers: dict = None) -> requests.Response:
    headers = config.headers if not headers else None
    response = requests.put(url=url, data=data, headers=headers)
    try:
        if response.status_code == 200:
            response.encoding = 'utf-8'
        return response
    except:
        return False


def delete(url, data=None, headers: dict = None) -> requests.Response:
    headers = config.headers if not headers else None
    response = requests.delete(url=url, data=data, headers=headers)
    try:
        if response.status_code == 200:
            response.encoding = 'utf-8'
        return response
    except:
        return False


async def async_get():
    return


async def async_post():
    return


async def async_put():
    return


async def async_delete():
    return


if __name__ == '__main__':
    res = get('https://www.baidu.com/')
    print(res.text)
