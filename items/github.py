#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: v0.0.1
@author: James Yang
@license: MIT License
@email: i@white-album.top
@blog: https://white-album.top
@software: PyCharm
@file: github.py
@time: 2020/2/7 20:27
"""
from bs4 import BeautifulSoup
from lxml import etree
import requests

cdn = 'https://cdn.jsdelivr.net/gh/jamesyangget/LickingDogAPI/data/'
languages = requests.get(cdn+'language.json').json()
spoken_langs = requests.get(cdn+'spoken_language.json').json()
date_type = ['daily', 'weekly', 'monthly']
xpath_list = ['//img/@src', '//a', '//a/@href', '//div', '//p']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.130 Safari/537.36 Edg/79.0.309.71'
}


class Options(object):
    """
    @:param type 榜单类型
    @:param spoken_lang 地区语言
    @:param lang 编程语言
    @:param date 时间范围
    """
    type: str
    spoken_lang: str
    lang: str
    date: str


def full_url(options):
    trending = 'https://github.com/trending'
    developers = trending + '/developers'
    url = ''
    if options.type == 'trending':
        for i in languages:
            if options.lang == i['language'] and (options.date in date_type):
                for j in spoken_langs:
                    if options.spoken_lang == j['spoken_language']:
                        url = trending + '/{}?since={}&spoken_language_code={}'.format(
                            options.lang, options.date, options.spoken_lang)
            else:
                for j in spoken_langs:
                    if options.spoken_lang == j['spoken_language']:
                        url = trending + '/{}?since=daily&spoken_language_code={}'.format(
                            options.lang, options.spoken_lang)
        else:
            if options.date:
                url = trending + '?since={}'.format(options.date)
    elif options.type == 'developers':
        for i in languages:
            if options.lang == i['language'] and options.date in date_type:
                url = developers + '/{}?since={}'.format(options.lang,options.date)
            else:
                url = developers + '/{}?since=daily'.format(options.lang)
        else:
            if options.date:
                url = developers + '?since={}'.format(options.date)
    return url


def dom_parse(html, xpath):
    dom_tree = etree.HTML(html)
    return dom_tree.xpath(xpath)


class Github(object):
    @classmethod
    def trending(cls, options):
        url, data = full_url(options), []
        html = requests.get(url, headers=headers).content.decode('utf-8')
        articles = BeautifulSoup(html, 'lxml').find_all('article', {'class': 'Box-row'})
        for article in articles:
            html = str(article.find('h1', {'class': 'h3 lh-condensed'}))
            _, username, repo = dom_parse(html, xpath_list[2])[0].split('/')
            description = dom_parse(str(article), xpath_list[4])[0].text.strip()
            lang = article.find('span', {'itemprop': 'programmingLanguage'})
            lang = None if lang is None else lang.text
            info = article.find_all('a', {'class': 'muted-link d-inline-block mr-3'})
            star = info[0].text.strip().replace(',', '')
            fork = info[1].text.strip().replace(',', '')
            data.append({
                "username": username,
                "repo": repo,
                "description": description,
                "language": lang,
                "star": star,
                "fork": fork
            })
        return data

    @classmethod
    def developers(cls, options):
        url, data = full_url(options), []
        html = requests.get(url, headers=headers).content.decode('utf-8')
        articles = BeautifulSoup(html, 'lxml').find_all('article', {'class': 'Box-row d-flex'})
        for article in articles:
            rank = articles.index(article) + 1  # 排位
            avatar = dom_parse(html, xpath_list[0])[0]  # 头像
            name = str(article.find('h1', {'class': 'h3 lh-condensed'}))
            article = str(article.find('article'))
            _, username, repo = dom_parse(article, xpath_list[2])[0].split('/')  # 用户名和最受欢迎的仓库名
            nickname = dom_parse(name, xpath_list[1])[0].text.strip()  # 昵称
            description = dom_parse(article, xpath_list[3])[1].text.strip()  # 仓库描述
            print(description)
            data.append({
                "rank": rank,
                "avatar": avatar,
                "nickname": nickname,
                "username": username,
                "repo": repo,
                "description": description
            })
        return data


if __name__ == '__main__':
    pass
