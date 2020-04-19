from enum import Enum


class Charts(str, Enum):
    hot100 = 'hot-100'
    billboard200 = 'billboard-200'
    artist100 = 'artist-100'
    social50 = 'social-50'


class Music(object):
    class Service(str, Enum):
        cloudmusic: str = "cloudmusic"
        qq: str = "qq"

    class Type(str, Enum):
        song: str = "song"
        lyric: str = "lyric"
        playlist: str = "playlist"
