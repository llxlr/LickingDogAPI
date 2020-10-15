#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bilibili_api
from bilibili_api import aid2bvid, Verify, video, user
from config import sessdata, bili_jct

bilibili_api.request_settings = {
    "use_https": True,
    "proxies": {}
}
verify = Verify(sessdata=sessdata, csrf=bili_jct)


class Bilibili(object):
    def __init__(self, vid=None, date=None):
        """
        :param vid: 视频的aid或bvid号
        :param date: 时间
        """
        self.vid = vid
        self.date = date

    def av2bv(self):
        return self.vid if 'BV' in self.vid else aid2bvid(self.vid)

    def get_video_info(self):
        """"""
        self.vid = self.vid if 'av' in self.vid else self.av2bv()
        v = video.get_video_info(bvid=self.vid, verify=verify)
        return v

    def get_video_url(self, page=0):
        """获取视频直链"""
        url = video.get_download_url(bvid=self.vid, page=page, verify=verify)
        return url

    def get_danmaku(self):
        """获取视频特定时间的弹幕"""
        danmaku = video.get_danmaku(bvid=self.vid, date=self.date, verify=verify)
        return danmaku

    def get_bangumi(self):
        """获取番剧信息"""
        pass

    @classmethod
    def get_user_bangumi(cls, uid, type_, pn=None):
        """获取用户订阅"""
        if pn is not None:
            bgm = user.get_bangumi_raw(uid=uid, pn=pn, ps=15, type_=type_, verify=verify)
            bgm = bgm['list']
        else:
            bgm = user.get_bangumi(uid=uid, type_=type_, verify=verify)
        # bgm = {
        #     'title': bgm['title'],
        #     'desc': bgm['evaluate'],
        #     'cover': bgm['cover'],
        #     'badge': bgm['badge'],
        #     'type': bgm['season_type_name'],
        #     'area': bgm['areas']['name'],
        #     'watch_state': bgm['progress'],
        #     'publish_state': bgm['new_ep']['index_show']
        # }
        return bgm


if __name__ == '__main__':
    # https://passkou.com/docs/bilibili_api/
    # bili = Bilibili(vid="BV1uv411q7Mv")
    # print(bili.get_danmaku())
    # print(bili.get_video_url())
    bgm = Bilibili().get_user_bangumi(166791985, 'bangumi')
    print(bgm)
    pass
