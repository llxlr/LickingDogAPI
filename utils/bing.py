#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: v0.0.1
@author: James Yang
@license: MIT License
@email: i@white-album.top
@blog: https://white-album.top
@software: PyCharm
@file: bing.py
@time: 2020/2/7 21:22
"""
from bs4 import BeautifulSoup
import requests
import json
import re

bing = 'https://cn.bing.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.130 Safari/537.36 Edg/79.0.309.71'
}


def response(url):
    res = requests.get(url, headers=headers, allow_redirects=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


class Image(object):
    soup = response(bing)
    bglink = re.search(r'href="(.*?)"', str(soup.find('link', {'id': 'bgLink'})))
    bglink = bing + bglink.group(1).replace('&amp;rf=LaDigue_1920x1080.jpg&amp;pid=hp', '')

    @classmethod
    def img(cls):
        return cls.bglink

    @classmethod
    def info(cls):
        sh_cp = str(cls.soup.find('a', {'id': 'sh_cp'}))
        title = re.search(r'title="(.*?)"', sh_cp).group(1)
        href = bing + re.search(r'href="(.*?)"', sh_cp).group(1)
        return {'img': cls.bglink, 'info': {'title': title, 'search': href}}


if __name__ == '__main__':
    print(Image.img())
    print(json.dumps(Image.info(), indent=4))
