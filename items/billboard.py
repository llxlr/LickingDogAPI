#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: v0.0.1
@author: James Yang
@license: MIT License
@email: i@white-album.top
@blog: https://white-album.top
@software: PyCharm
@file: billboard.py
@time: 2020/2/20 7:13
"""
from lxml import etree
import requests

url = 'https://www.billboard.com/charts/'

xpr = [
    '//span[@class="chart-element__information__song text--truncate color--primary"]/text()',
    '//span[@class="chart-element__information__artist text--truncate color--secondary"]/text()',
    '//span[@class="chart-element__information__delta__text text--default"]/text()',
    '//span[@class="chart-element__information__delta__text text--last"]/text()',
    '//span[@class="chart-element__information__delta__text text--peak"]/text()',
    '//span[@class="chart-element__information__delta__text text--week"]/text()',
    '//span[@class="chart-element__image flex--no-shrink"]/@style',
]
type_ = ['song', 'artist', 'now', 'last', 'peak', 'week', 'avater']
data = []


def parse(htm):
    htm = etree.HTML(htm)
    single = {}
    for xp in xpr:
        n = xpr.index(xp)
        for content in htm.xpath(xp):
            if n in [0, 1, 2]:
                single[type_[n]] = content
            elif n in [3, 4, 5]:
                single[type_[n]] = content.split(' ')[0]
            elif n == 6:
                if not content.split('"'):
                    single[type_[n]] = content.split('"')[1]
    return single


def get_content(chart):
    html = requests.get(url+chart).content
    selector = etree.HTML(html)
    lis = selector.xpath('//ol[@class="chart-list__elements"]/li')
    for li in map(lambda x: etree.tostring(x, encoding='utf-8').decode('utf-8'), lis):
        data.append(parse(li))
    return data


if __name__ == '__main__':
    pass
