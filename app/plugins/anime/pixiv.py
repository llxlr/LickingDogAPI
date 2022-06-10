#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import PIXIV_USERNAME, PIXIV_PASSWD, PIXIV_REFRESH_TOKEN
from pixivpy3 import *
import requests

main_url = "https://www.pixiv.net"
headers = {
    'User-Agent': 'PixivAndroidApp/5.0.64 (Android 6.0)',
    'Content-Type': 'application/x-www-form-urlencoded'
}
# client = PixivClient()
# aapi = AppPixivAPI(client=client.start())
# papi = PixivAPI(client=client)
# aapi.login(PIXIV_EMAIL, PIXIV_PASSWD)
# papi.login(PIXIV_EMAIL, PIXIV_PASSWD)


def connent():
    try:
        r = requests.get(main_url, headers=headers)
        if r.status_code == 200:
            return True
    except Exception as e:
        del e
        return False


# class Pixiv:
#     def __init__(self, id=None, text=None):
#         self.id, self.text = id, text
#
#     def works(self):
#         return papi.works(self.id)
#
#     def search(self):
#         return papi.search_works(self.text, page=1, mode='text')


if __name__ == "__main__":
    print(connent())
    pass
