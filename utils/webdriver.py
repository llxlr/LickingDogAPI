#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

python webdriver.py $()

"""
from lxml import etree
import requests
import sys

if len(sys.argv) > 2:
    print('You have specified too many arguments!')
    sys.exit()
elif len(sys.argv) < 2:
    print('You need to input Chrome Version!')
    sys.exit()
elif sys.argv[0] != __file__:
    print('It\'s like "python webdriver.py CHROME_VERSION"')
    sys.exit()

if sys.platform.startswith('linux'):
    pkg = 'chromedriver_linux64.zip'
elif sys.platform.startswith('darwin'):
    pkg = 'chromedriver_mac64.zip'
elif sys.platform.startswith('win32'):
    pkg = 'chromedriver_win32.zip'
else:
    print('Unsupport Operating System!')
    sys.exit()

url = 'https://npm.taobao.org/mirrors/chromedriver'
version = sys.argv[1]
a, b, c, d = version.split('.')

res = requests.get(
    url,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38'}
)
res.encoding = 'utf-8'
html = etree.HTML(res.text)

links = []
for link in html.xpath('//pre/a/@href'):
    if 'LATEST_RELEASE' not in link and 'index.html' not in link and 'icons' not in link:
        v = link.split('/')[-2]
        # print(v.split('.'))
        if len(v.split('.')) == 4:
            # print(v.split('.'))
            e, f, g, h = v.split('.')
            if version in v:
                # print(version)
                links.append(version)
            elif a+b+c == e+f+g:
                # print(v)
                links.append(v)
            elif a == e:
                # print(v)
                links.append(version)

if len(links) > 1:
    version = links[-1]
else:
    version = links[0]

print(f"{url}/{version}/{pkg}")