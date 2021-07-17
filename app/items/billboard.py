#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
import requests

from config import headers

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
single, data = {}, []

def parse(html):
    selector = etree.HTML(html)
    for idx, xp in enumerate(xpr):
        for content in selector.xpath(xp):
            if idx in [0, 1, 2]:
                single[type_[idx]] = content
            elif idx in [3, 4, 5]:
                single[type_[idx]] = content.split(' ')[0]
            elif idx == 6:
                if not content.split('"'):
                    single[type_[idx]] = content.split('"')[1]
    return single


def get_content(chart):
    html = requests.get(url+chart, headers=headers).content
    selector = etree.HTML(html)
    lis = selector.xpath('//ol[@class="chart-list__elements"]/li')
    for li in map(lambda x: etree.tostring(x, encoding='utf-8').decode('utf-8'), lis):
        data.append(parse(li))
    return data
