#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: v0.0.1
@author: James Yang
@license: MIT License
@email: i@white-album.top
@blog: https://white-album.top
@software: PyCharm
@file: cloudmusic.py
@time: 2020/2/7 16:39
"""
import requests
# import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.130 Safari/537.36 Edg/79.0.309.71'
}


class CloudMusic(object):
    @classmethod
    def song(cls, id_: int):
        url = "https://music.163.com/song/media/outer/url?id={}.mp3".format(id_)
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code == 302:
            redirect_url = res.headers["Location"]
            return redirect_url if 'https:' in redirect_url else redirect_url.replace('http', 'https')
        else:
            return res.status_code

    @classmethod
    def lyric(cls, id_: int):
        url = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'.format(id_)
        res = requests.get(url, headers=headers)
        data = res.json()
        if data["code"] == 200:
            if "lrc" in data:
                lrc = data["lrc"]["lyric"]
                return lrc
            elif "nolyric" in data:
                return ''
            elif "uncollected" in data:
                return None

    @classmethod
    def playlist(cls, id_: int):
        url = 'https://music.163.com/api/playlist/detail?id={}'.format(id_)
        res = requests.get(url, headers=headers).json()
        if res["code"] == 200:
            data = []
            for item in res['result']['tracks']:
                item_format = {
                    'name': item['name'],
                    'id': item['id'],
                    'artists': list(artist['name'] for artist in item['artists']),
                    'album': {
                        'name': item['album']['name'],
                        'artists': list(artist['name'] for artist in item['album']['artists'])
                    },
                    'url': cls.song(item['id']),
                    'cover': str(item['album']['picUrl']).replace('http:', 'https:'),
                    'lrc': cls.lyric(item['id'])
                }
                data.append(item_format)
            return data
    pass


class QQ(object):
    @classmethod
    def song(cls, id_: int):
        pass

    @classmethod
    def lyric(cls, id_: int):
        pass

    @classmethod
    def playlist(cls, id_: int):
        pass


# if __name__ == "__main__":
    # s = time.time()
    # print(playlist(3196408340))  # 5s~6s
    # print(lyric(412327036))      # 0.1s~0.2s
    # print(CloudMusic.song(1415756555))      # 0.2s~0.4s
    # e = time.time()
    # print(e-s)
