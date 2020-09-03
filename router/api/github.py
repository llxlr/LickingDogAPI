from items.github import Github
from fastapi import APIRouter
from config import log, Copyright
import time
router = APIRouter()


@router.get("/trending/")
async def trending(
        type: str = "trending",
        date: str = "daily",
        spoken_lang: str = None,
        language: str = None):

    log.info("pv,请求一次Github Trending")
    if type in ['trending', 'developers']:
        return {
            "code": 200,
            "Copyright": Copyright,
            "data": Github(type, date, None, language).trending if type == 'trending'
            else Github(type, date, spoken_lang, language).developers,
            "time": time.ctime(),
        }