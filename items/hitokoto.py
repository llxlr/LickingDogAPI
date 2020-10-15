#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import headers, cdn
from random import randint
import requests


def hitokoto():
    """一言"""
    data = requests.get(cdn + 'hitokoto.json', headers=headers).json()
    return data[randint(1, len(data))]


def poem():
    """每日诗词"""
    _svg = '<svg xmlns="http://www.w3.org/2000/svg" height="22.0" width="342.5"><g><text text-anchor="start" ' \
           'letter-spacing="1.5" font-smoothing="antialiased" ' \
           'font-family="KaiTi,Segoe UI,Lucida Grande,Helvetica,Arial,Microsoft YaHei,FreeSans,' \
           'Arimo,Droid Sans,wenquanyi micro hei,Hiragino Sans GB,Hiragino Sans GB W3,sans-serif" ' \
           'font-size="{}" id="svg_1" y="20.0" x="0" stroke-width="0" stroke="#000" ' \
           'fill="#000000"></text></g></svg>'
    pass


def dog():
    """舔狗日记"""
    pass
