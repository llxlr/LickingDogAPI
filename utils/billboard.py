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
charts = ['hot-100', 'billboard-200', 'artist-100', 'social-50']
xpathRule = [
    '//span[@class="chart-element__information__song text--truncate color--primary"]/text()',
    '//span[@class="chart-element__information__artist text--truncate color--secondary"]/text()',
    '//span[@class="chart-element__information__delta__text text--default"]/text()',
    '//span[@class="chart-element__information__delta__text text--last"]/text()',
    '//span[@class="chart-element__information__delta__text text--peak"]/text()',
    '//span[@class="chart-element__information__delta__text text--week"]/text()',
    '//span[@class="chart-element__image flex--no-shrink"]/@style',
]


def get_content(url_, xpaths):
    html = requests.get(url_).content
    selector = etree.HTML(html)
    data, single = [], {'song': '', 'artist': '', 'now': '', 'last': '', 'peak': '', 'week': '', 'avater': ''}
    for xp in xpaths:
        for content in selector.xpath(xp):
            if xpaths.index(xp) == 0:
                single['song'] = content
            elif xpaths.index(xp) == 1:
                single['artist'] = content
            elif xpaths.index(xp) == 2:
                single['now'] = content
            elif xpaths.index(xp) == 3:
                single['last'] = content.split(' ')[0]
            elif xpaths.index(xp) == 4:
                single['peak'] = content.split(' ')[0]
            elif xpaths.index(xp) == 5:
                single['week'] = content.split(' ')[0]
            elif xpaths.index(xp) == 6:
                if not content.split('"'):
                    single['avater'] = content.split('"')[1]
            data.append(single)
    return data


class Billboard(object):
    def __init__(self, chart):
        super(Billboard, self).__init__()
        self.chart = chart

    def info(self):
        if self.chart == charts[0]:
            return get_content(url+self.chart, xpathRule)
        elif self.chart == charts[1]:
            return get_content(url+self.chart, xpathRule)
        elif self.chart == charts[2]:
            return get_content(url+self.chart, xpathRule)
        elif self.chart == charts[3]:
            return get_content(url+self.chart, xpathRule)


if __name__ == '__main__':
    # tobject = get_content(url + 'hot-100', xpathRule)
    tobject = Billboard('hot-100').info()
    print(tobject)  # ↑↓→.xpath(button[0]
