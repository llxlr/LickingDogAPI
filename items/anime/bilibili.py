import bilibili_api
from bilibili_api import aid2bvid, Verify, video
from settings import sessdata, bili_jct

bilibili_api.request_settings = {
    "use_https": True,
    "proxies": None
}
verify = Verify(sessdata=sessdata, csrf=bili_jct)


class Bilibili(object):
    def __init__(self, vid, date=None):
        """
        :param vid: 视频的aid和bvid号
        :param date: 时间
        """
        self.vid = vid
        self.date = date

    def av2bv(self):
        return self.vid if 'BV' in self.vid else aid2bvid(self.vid)

    def get_video_info(self):
        """"""
        self.vid = self.vid if 'av' in self.vid else self.av2bv()
        v = video.get_video_info(bvid=self.vid)
        return v

    def get_video_url(self):
        """获取视频直链"""
        url = video.get_download_url(bvid=self.vid)
        return url

    def get_danmaku(self):
        """获取视频特定时间的弹幕"""
        danmaku = video.get_danmaku(bvid=self.vid, date=self.date)
        return danmaku


if __name__ == '__main__':
    # https://passkou.com/docs/bilibili_api/
    bili = Bilibili(vid="BV1uv411q7Mv")
    # print(bili.get_danmaku())
    print(bili.get_video_url())
    pass
