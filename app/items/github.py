#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://docs.github.com/cn/rest

https://docs.github.com/cn/graphql
"""
import json

from lxml import etree
import requests

from config import headers, cdn
import data

# languages, spoken_langs = requests.get(cdn+'gh-trending.json', headers=headers).json()
with open(data.github_trending(), 'r') as ff:
    data = json.load(ff)
    languages, spoken_langs = data["languages"], data["spoken_languages"]
xp = [
    # trending
    '//article[@class="Box-row"]',  # 项目总榜
    '//h1[@class="h3 lh-condensed"]/a/@href',  # user, repo
    '//p/text()',  # description
    '//span[@itemprop="programmingLanguage"]/text()',  # language
    '//a[@class=" muted-link d-inline-block mr-3"]',  # star, fork
    # developers
    '//article[@class="Box-row d-flex"]',  # 开发者总榜
    '//img[@class="rounded-1"]/@src',  # avatar
    '//h1[@class="h3 lh-condensed"]/a/text()',  # nickname
    '//p[@class="f4 text-normal mb-1"]/a/text()',  # username
    '//h1[@class="h4 lh-condensed"]/a/text()',  # repo
    '//div[@class="f6 text-gray mt-1"]/text()',  # description
]


def url(type_, date, spoken_lang, language):
    trending = 'https://github.com/trending'
    developers = trending + '/developers'
    url_ = ''
    if type_ == 'trending':
        url_ = trending
        if list(filter(lambda x: x["language"] == language, languages)):
            if list(filter(lambda x: x["spoken_language"] == spoken_lang, spoken_langs)):
                if date in ['daily', 'weekly', 'monthly']:
                    url_ += f'/{language}?since={date}&spoken_language_code={spoken_lang}'
            else:
                url_ += f'/?since={date}&spoken_language_code={spoken_lang}' if date in ['daily', 'weekly', 'monthly'] else ''
        else:
            url_ += f'/?since={date}' if date in ['daily', 'weekly', 'monthly'] else ''
    elif type_ == 'developers':
        url_ = developers
        if list(filter(lambda x: x["language"] == language, languages)):
            url_ += f'/{language}?since={date}' if date in ['daily', 'weekly', 'monthly'] else ''
        else:
            url_ += f'/?since={date}' if date in ['daily', 'weekly', 'monthly'] else ''
    return url_


class Github(object):
    def __init__(self, type_, date, spoken_lang, language):
        self.type, self.date, self.spoken_lang, self.language = type_, date, spoken_lang, language

    def trending(self):
        url_, data = url(self.type, self.date, self.spoken_lang, self.language), []
        list_ = etree.HTML(requests.get(url_, headers=headers).text).xpath(xp[0])
        for frame in list_:
            frame = etree.HTML(bytes.decode(etree.tostring(frame)))
            _ = frame.xpath(xp[1])
            user, repo = _[0][1:].split('/')
            _ = frame.xpath(xp[2])
            description = _[0].strip() if _ else ''
            _ = frame.xpath(xp[3])
            language = _[0] if _ else ''
            _ = frame.xpath(xp[4])
            star = fork = ''
            for __ in _:
                ___ = __.xpath('//svg[@aria-label="star"]')
                star = bytes.decode(etree.tostring(___[0])).split('\n')[-2].strip() if ___ else ''
                ___ = __.xpath('//svg[@aria-label="fork"]')
                fork = bytes.decode(etree.tostring(___[0])).split('\n')[-2].strip() if ___ else ''
            data.append({"username": user, "repo": repo, "description": description,
                        "language": language, "star": star, "fork": fork})
        return data

    def developers(self):
        url_, data = url(self.type, self.date, self.spoken_lang, self.language), []
        list_ = etree.HTML(requests.get(url_, headers=headers).text).xpath(xp[5])
        for frame in list_:
            frame = etree.HTML(bytes.decode(etree.tostring(frame)))
            avatar = frame.xpath(xp[6])[0]
            nickname = frame.xpath(xp[7])[0].strip()
            username = frame.xpath(xp[8])[0].strip()
            repo = frame.xpath(xp[9])[0].strip()
            description = frame.xpath(xp[10])[0].strip()
            data.append({"avatar": avatar, "nickname": nickname, "username": username,
                        "repo": repo, "description": description})
        return data


if __name__ == '__main__':
    # print(url("trending", "daily", None, None))
    # print(Github("trending", "daily", None, None).trending())
    # print(url("developers", "daily", None, None))
    print(Github("developers", None, None, "daily").developers())
    pass
