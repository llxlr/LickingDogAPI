#!/usr/bin/env python
# -*- coding: utf-8 -*-
from items.github import Github
from fastapi import APIRouter
from config import *
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
            "status": 200,
            "copyright": Copyright,
            "data": Github(type, date, None, language).trending if type == 'trending'
            else Github(type, date, spoken_lang, language).developers,
            "time": time.ctime(),
        }
