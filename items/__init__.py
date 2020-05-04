from enum import Enum


class Charts(str, Enum):
    hot100: str = 'hot-100'
    billboard200: str = 'billboard-200'
    artist100: str = 'artist-100'
    social50: str = 'social-50'


class Music(object):
    class Service(str, Enum):
        cloudmusic: str = "cloudmusic"
        qq: str = "qq"

    class Type(str, Enum):
        song: str = "song"
        lyric: str = "lyric"
        playlist: str = "playlist"


class NcovName(str, Enum):
    china: str = 'china'
    world: str = 'world'
