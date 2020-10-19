#!/usr/bin/env python
# -*- coding: utf-8 -*-
from starlette.middleware.cors import CORSMiddleware  # Cross-Origin Resource Sharing
from starlette.templating import Jinja2Templates  # Templates
from starlette.staticfiles import StaticFiles  # Static
from fastapi.openapi.utils import get_openapi  # custom openapi
from fastapi import FastAPI, APIRouter
from .api import github, music, user, tools
from config import *
api_router = APIRouter()
app = FastAPI(
    title=hometitle,
    description=description,
    version=docv,
    openapi_url=f'{version}/openapi.json',
    docs_url=f'{version}/docs/',
    redoc_url=None
)


def custom_schema():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(title=hometitle,
                                 version=docv,
                                 description=description,
                                 routes=app.routes)
    openapi_schema["info"]["x-logo"] = {
        "url": "https://cdn.jsdelivr.net/gh/llxlr/cdn/img/2020/02/08/f7dpek.jpg"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_schema
app.add_middleware(
    CORSMiddleware,  # 添加跨域中间件
    # allow_origins=config.origins,  # 允许跨域请求的域名列表
    allow_origin_regex=origin_regex,  # 允许跨域请求的域名正则表达式
    allow_credentials=True,  # 在跨域请求时是否支持cookie
    allow_methods=["*"],  # 允许跨域请求的HTTP方法列表
    allow_headers=["*"],  # 跨域请求支持的HTTP头信息列表
    expose_headers=[],  # 对浏览器可见的返回结果头信息，默认为[]
    max_age=60,  # 浏览器缓存CORS返回结果的最大时长，默认为600(单位秒)
)
app.mount("/static", StaticFiles(directory="static", packages=[]), name="static")  # 静态资源设置
api_router.include_router(user.router, tags=["users"])
api_router.include_router(music.router, prefix='/music', tags=["music"])
api_router.include_router(github.router, prefix='/github', tags=["github"])
api_router.include_router(tools.router, tags=["tools"])
app.include_router(api_router, prefix=version)
templates = Jinja2Templates(directory="templates")  # 页面模板
