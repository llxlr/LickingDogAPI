from enum import Enum


class Charts(str, Enum):
    """榜单类型"""
    hot100: str = 'hot-100'
    billboard200: str = 'billboard-200'
    artist100: str = 'artist-100'
    social50: str = 'social-50'


class Music(object):
    class Service(str, Enum):
        """音乐服务商"""
        cloudmusic: str = "cloudmusic"
        qq: str = "qq"

    class Type(str, Enum):
        """分类"""
        song: str = "song"
        lyric: str = "lyric"
        playlist: str = "playlist"


class NcovName(str, Enum):
    """新冠肺炎地区"""
    china: str = 'china'
    world: str = 'world'
