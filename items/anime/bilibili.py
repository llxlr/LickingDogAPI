from settings import headers
from utils.funcation import delay
import requests
import os

table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr = {table[i]: i for i in range(58)}
s = [11, 10, 3, 8, 4, 6]
xor, add = 177451812, 8728348608


def av2bv(uid):
    uid = (uid ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[uid // 58 ** i % 58]
    return ''.join(r)


def bv2av(uid):
    r = 0
    for i in range(6):
        r += tr[uid[s[i]]] * 58 ** i
    return (r - add) ^ xor


class Bangumi(object):
    def __init__(self, uid, pn, ps, ts=1584480325628):
        self.url = 'https://api.bilibili.com/x/space/bangumi/follow/list?type=1' + \
                   f'&pn={pn}&ps={ps}&vmid={uid}&ts={ts}'

    def __get(self):
        return requests.get(self.url, headers=headers).json()

    def data(self):
        raw, data = self.__get(), []
        if raw['code'] == 0:
            raw = raw['data']['list']
        for i in raw:
            data.append({'season_id': i['season_id'],
                        'season_type_name': i['season_type_name'],
                         'title': i['title'],
                         'cover': i['cover'],
                         'new_ep': {'id': i['new_ep']['id'],
                                    'index_show': i['new_ep']['index_show'],
                                    'cover': i['new_ep']['cover'],
                                    'long_title': i['new_ep']['long_title'] if 'long_title' in i['new_ep'] else '',
                                    'pub_time': i['new_ep']['pub_time']},
                         'evaluate': i['evaluate'],
                         'areas': i['areas']})
        return data


if __name__ == '__main__':
    pn = 1
    ps = 15
    uid = 166791985
    bgm = Bangumi(uid, pn, ps)
    print(bgm.data())
