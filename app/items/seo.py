#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import ua
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree


def driver(url: str):
    """实例化driver"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument(f"user-agent='{ua.random}'")
    wd = webdriver.Chrome(options=options)
    wd.get(url)
    return wd


def baidu(url):
    wd = driver('https://www.baidu.com/s?wd='+url)
    html = etree.HTML(wd.page_source)
    value = html.xpath('//span[@class="nums_text"]')[0]
    return value


print(baidu('site:white-album.top'))
