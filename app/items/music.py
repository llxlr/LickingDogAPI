#!/usr/bin/env python
# -*- coding: utf-8 -*-
from starlette.status import HTTP_404_NOT_FOUND
from starlette.responses import JSONResponse
import requests

from config import headers
from items import Music


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


def music_type(classname, type: str, id):
    if type == Music.Type.song:
        return classname.song(id)
    elif type == Music.Type.lyric:
        return classname.lyric(id)
    elif type == Music.Type.playlist:
        return classname.playlist(id)
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND, content=type)


if __name__ == "__main__":
    pass
