#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, File, UploadFile
from plugins.github import Github
from utils.spider import put, delete
from config import *
import time
router = APIRouter()


@router.get("/trending/", include_in_schema=True)
async def trending(type: str = "trending",
                   date: str = "daily",
                   spoken_lang: str = None,
                   language: str = None):
    log.info("pv,请求一次Github Trending")
    if type in ['trending', 'developers']:
        github = Github(type, date, spoken_lang, language)
        return {
            "status": 200,
            "copyright": Copyright,
            "data": github.trending if type == 'trending' else github.developers,
            "time": time.ctime(),
        }


@router.post('/upload/', include_in_schema=True)
async def upload(user, email, token, repo, path='', file: UploadFile = File(...)):
    if file.filename:
        log.info(f'pv,上传文件{file.filename}')
        url = f'https://api.github.com/repos/{user}/{repo}/contents/{path+file.filename}'
        data = {
            "message": "upload By LickingDogAPI",
            "committer": {
                "name": user,
                "email": email
            },
            "content": file
        }
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
            "User-Agent": ua.random,
            "Authorization": f"token {token}"
        }
        # PUT https://api.github.com/repos/{user}/{repo}/contents/{path}/{filename}
        response = put(url=url, data=data, headers=headers)
        return response.json()


@router.delete('/delete/', include_in_schema=True)
async def delete(user, repo, token, path='', filename=File(...)):
    url = f'https://api.github.com/repos/{user}/{repo}/contents/{path+filename}'
    # DELETE https://api.github.com/repos/{user}/{repo}/contents/{path}/{filename}
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
        "User-Agent": ua.random,
        "Authorization": f"token {token}"
    }
    response = delete(url=url, data=None, headers=headers)
    return response.json()
