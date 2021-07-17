#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://gist.github.com/upbit/6edda27cb1644e94183291109b8a5fde
https://hub.fastgit.org/upbit/pixivpy/blob/master/example_bypass_sni.py
"""
import asyncio

from pixivpy_async import PixivClient, AppPixivAPI

from config import PIXIV_USERNAME, PIXIV_PASSWD

proxy = ''


async def main():
    async with PixivClient(limit=30, timeout=10, proxy=proxy) as client:
        app_api = AppPixivAPI(client=client)
        # 登录
        await app_api.login(username=PIXIV_USERNAME, password=PIXIV_PASSWD)
        a = await app_api.illust_detail(59580629)
        print(a)

if __name__ == '__main__':
    asyncio.run(main())
