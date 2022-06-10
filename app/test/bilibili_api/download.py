#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import asyncio

from bilibili_api import video, Credential
import aiohttp
import aiofiles

from config import sessdata, bili_jct, buvid3

SAVE_PATH = 'E:/Downloads/Video'
FFMPEG_PATH = 'ffmpeg'
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://www.bilibili.com/'
}


async def download_stream(session: aiohttp.ClientSession, url: str, name: str):
    async with session.get(url, headers=headers) as resp:
        length = resp.headers.get('content-length')
        async with aiofiles.open(name, 'wb') as f:
            process = 0
            while True:
                chunk = await resp.content.read(1024)
                if not chunk:
                    break
                process += len(chunk)
                print(f'下载{name} {process} / {length}')
                await f.write(chunk)


async def main(bvid):
    credential = Credential(sessdata=sessdata, bili_jct=bili_jct, buvid3=buvid3)  # 实例化 Credential 类
    v = video.Video(bvid=bvid, credential=credential)  # 实例化 Video 类
    url = await v.get_download_url(0)  # 获取视频下载链接
    video_url = url['dash']['video'][0]['baseUrl']  # 视频轨链接
    audio_url = url['dash']['audio'][0]['baseUrl']  # 音频轨链接
    async with aiohttp.ClientSession() as session:
        await download_stream(session, video_url, f'{SAVE_PATH}/video_temp.m4s')  # 下载视频流
        await download_stream(session, audio_url, f'{SAVE_PATH}/audio_temp.m4s')  # 下载音频流
        # 混流
        print('混流中')
        os.system(f'{FFMPEG_PATH} -i {SAVE_PATH}/video_temp.m4s -i {SAVE_PATH}/audio_temp.m4s '
                  f'-vcodec copy -acodec copy {SAVE_PATH}/video.mp4')

        # 删除临时文件
        os.remove(f'{SAVE_PATH}/video_temp.m4s')
        os.remove(f'{SAVE_PATH}/audio_temp.m4s')

        print('已下载为：video.mp4')


if __name__ == '__main__':
    asyncio.run(main('BV1V64y197tj'))
