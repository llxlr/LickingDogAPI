#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi.responses import HTMLResponse, ORJSONResponse, RedirectResponse
from fastapi.requests import Request
from .media import app, templates
from config import *


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home(request: Request):
    log.info('ts,访问一次主页')
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": title,
        "keywords": "API,舔狗,舔狗API,Licking Dog API,接口,FastAPI,Awesome",
        "description": description,
        "version": version,
        "author": Copyright["author"],
        "analysis": analysis,
        "gitalk_config": gitalk_config,
    })


@app.get("/admin/", response_class=HTMLResponse, include_in_schema=False)
async def admin(request: Request):
    log.info('ts,访问一次后台管理')
    return templates.TemplateResponse("admin/index.html", {
        "request": request,
        "title": "后台管理 - "+title,
        "keywords": "后台管理",
        "description": "后台管理",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/login/", response_class=HTMLResponse, include_in_schema=False)
async def admin(request: Request):
    log.info('ts,访问一次用户登录')
    return templates.TemplateResponse("admin/login.html", {
        "request": request,
        "title": "用户登录 - "+title,
        "keywords": "用户登录",
        "description": "用户登录",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get('/limit.html', response_class=HTMLResponse, include_in_schema=False)
async def limit(request: Request):
    log.info('页面访问限制')
    return templates.TemplateResponse("limit.html", {
        "request": request,
    })


@app.get('/policy.html', response_class=HTMLResponse, include_in_schema=False)
async def policy(request: Request):
    log.info('ts,访问一次隐私政策页')
    return templates.TemplateResponse("policy.html", {
        "request": request,
        "title": "隐私政策",
        "keywords": "隐私政策,隐私保护,宣言,声明",
        "description": "用户隐私政策页面",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/bing/", response_class=ORJSONResponse, tags=["images"])
async def bing(type: str = None):
    import requests
    data = requests.get('https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1', headers=headers).json()
    img = {'src': 'https://cn.bing.com'+data["images"][0]["url"], 'copyright': data["images"][0]["copyright"]}
    log.info('pv,访问一次必应图片')
    return {"title": "Bing每日一图", "img": img} if type == 'img' else RedirectResponse(img['src'])


@app.get("/ncov.html", response_class=HTMLResponse, include_in_schema=False)
async def ncov(request: Request):
    log.info('ts,访问一次2020新冠肺炎实时疫情图')
    return templates.TemplateResponse("docs/items/ncov.html", {
        "request": request,
        "title": "2020新冠肺炎实时疫情图",
        "subtitle": "2020新冠肺炎实时疫情图",
    })
