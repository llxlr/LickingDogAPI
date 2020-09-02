from .bilibili import Bilibili
from .bangumi import Bangumi
from enum import Enum


class subscribe_category(str, Enum):
    """订阅类型"""
    bangumi: str = 'bangumi'
    drama: str = 'drama'
