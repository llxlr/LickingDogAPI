#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: v0.0.1
@author: James Yang
@license: MIT License
@email: i@white-album.top
@blog: https://white-album.top
@software: PyCharm
@file: hitokoto.py
@time: 2020/2/8 7:34
"""
import requests
from random import randint

cdn = 'https://cdn.jsdelivr.net/gh/jamesyangget/LickingDogAPI/data/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.130 Safari/537.36 Edg/79.0.309.71'
}
data = requests.get(cdn+'hitokoto.json', headers=headers).json()


def hitokoto():
    return data[randint(1, len(data))]
