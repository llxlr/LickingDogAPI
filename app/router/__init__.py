from router.pages import app
from enum import Enum


class CountDown(str, Enum):
    year: str
    color: str
    font_size: str
    font_family: str
