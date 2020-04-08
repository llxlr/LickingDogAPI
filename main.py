from fastapi import FastAPI, Form, File, UploadFile
from starlette.requests import Request
from fastapi.openapi.utils import get_openapi  # custom openapi
from starlette.staticfiles import StaticFiles  # Static
from starlette.templating import Jinja2Templates  # Templates
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND
from starlette.middleware.cors import CORSMiddleware  # Cross-Origin Resource Sharing
from enum import Enum
import uvicorn
import time
import settings

hometitle = "Licking Dog API"  # 主页标题
title404 = "404 Not Found"  # 404页标题
domain = "api.white-album.top"
port = 8001
docv = "1.0.0"  # doc版本
version = "/v" + docv[0]  # api版本
description = "简单功能的个人实现 | 舔狗API 🍭"  # api 描述
start_time = 2019  # 建站时间
_username = "admin"
_password = "admin"


def openapi_config(app: FastAPI):
    def _openapi_schema_custom():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title=hometitle,
            version=docv,
            description=description,
            routes=app.routes
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://img.white-album.top/i/2020/02/08/f7dpek.jpg"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema
    app.openapi = _openapi_schema_custom


def cors(app: FastAPI):
    origins = [
        f"http://{domain}",
        f"https://{domain}",
        "http://localhost",
        f"http://localhost:{port}"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


api = FastAPI(
    title=hometitle,
    description=description,
    version=docv,
    openapi_url=version+"/openapi.json",
    docs_url=version+"/docs/",
    redoc_url=None
)
openapi_config(api)  # openapi schemaz
api.mount("/static", StaticFiles(directory="static", packages=[]), name="static")  # 静态资源设置
templates = Jinja2Templates(directory="templates")  # 页面模板
cors(api)  # 解决跨域问题


@api.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": hometitle,
    })


@api.post("/login/")
async def login(*, username: str = Form(...), password: str = Form(...)):
    if username == _username and password == _password:
        return {
            "code": 200,
            "success": "true",
            "username": username, 
            "msg": "login successfully !",
            "time": time.ctime(),
        }
    return {
        "code": 404,
        "success": "false",
        "msg": "username or password is not correct !",
        "time": time.ctime(),
    }


@api.get("/start/")
async def start(request: Request):
    return templates.TemplateResponse("start.html", {
        "request": request,
        "title": "示例与说明",
    })


@api.get(version+"/bing/")
async def bing(request: Request):
    from items.bing import img
    return templates.TemplateResponse("bing.html", {
        "request": request,
        "title": "Bing每日一图",
        "info": img,
    })


@api.get("/mnist/")
async def mnist(request: Request):
    return templates.TemplateResponse("mnist.html", {
        "request": request,
        "title": "Tenserflow.js实现Mnist手写字识别",
    })


@api.get("/catvsdog/")
async def catvsdog(request: Request):
    return templates.TemplateResponse("catvsdog.html", {
        "request": request,
        "title": "Cat VS Dog",
    })


@api.get(version+"/github/")
async def trending(type_: str = "trending",
                   date: str = "daily",
                   spoken_lang: str = None,
                   language: str = None):
    from items.github import Options, Github
    options = Options()
    options.type, options.spoken_lang, options.lang, options.date = "trending", spoken_lang, language, date
    return Github.trending(options)


@api.get(version+"/github/trending/developers")
async def developers_trending(lang: str, date: str):
    from items.github import Options, Github
    options = Options()
    options.type, options.spoken_lang, options.lang, options.date = "developers", None, lang, date
    return Github.developers(options)


@api.get(version+"/music/{name}")
async def music(name: str, type: str, id: int):
    service = ["cloudmusic", "qq"]
    if name in service:
        if name == service[0]:
            from items.music import CloudMusic
            if type == "song":
                return CloudMusic.song(id)
            elif type == "lyric":
                return CloudMusic.lyric(id)
            elif type == "playlist":
                return CloudMusic.playlist(id)
            else:
                return JSONResponse(status_code=HTTP_404_NOT_FOUND, content=type)
        elif name == service[1]:
            from items.music import QQ
            if type == "song":
                return QQ.song(id)
            elif type == "lyric":
                return QQ.lyric(id)
            elif type == "playlist":
                return QQ.playlist(id)
            else:
                return JSONResponse(status_code=HTTP_404_NOT_FOUND, content=type)
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND, content=name)


class Charts(Enum):
    hot100: str = 'hot-100'
    billboard200: str = 'billboard-200'
    artist100: str = 'artist-100'
    social50: str = 'social-50'


@api.get(version+"/billboard/{chart}")
async def billboard(chart: str):
    from items.billboard import get_content
    if chart in [Charts.hot100,
                 Charts.billboard200,
                 Charts.artist100,
                 Charts.social50]:
        return get_content(chart)
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={'msg': f'{chart} is not found'})


# @api.post(version+"/files/")
# async def catvsdog_create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}


@api.post(version+"/catvsdog/upload/")
async def catvsdog_upload_image(file: UploadFile = File(...)):
    _format_ = ['image/bmp', 'image/gif', 'image/jpeg', 'image/jpg', 'image/png', 'image/x-icon']
    if file.filename != '':
        if file.content_type in _format_:
            return {
                "filename": file.filename,
                "content-type": file.content_type,
                "msg": "this is a {}, everything is ok !".format(file.content_type.split('/')[1]),
                "time": time.ctime(),
            }
    # text = await file.read()
    # await file.close()
    # return {
    #     "filename": file.filename,
    #     "content-type": file.content_type,
    #     "msg": "this is a {} file !".format(file_type[1]),
    #     "content": text,
    # }


@api.get('/purge-cdn-cache/')
async def purge_cdn_cache():
    import requests
    url = f"https://api.cloudflare.com/client/v4/zones/{settings.cf_zone_id}/purge_cache"
    headers = {
        "X-Auth-Email": f"{settings.cf_email}",
        "X-Auth-Key": f"{settings.cf_auth_key}",
        "Content-Type": "application/json"
    }
    post_data = '{"purge_everything": true}'
    res = requests.post(url, post_data, headers=headers).json()
    if res["success"]:
        return {
            "code": 200,
            "success": "true",
            "msg": "purge everything successfully !",
            "description": "clear cloudflare cdn caches",
            "time": time.ctime(),
        }


@api.get(version+'/hitokoto/{word}')
async def hitokoto(word: str = None):
    from items.hitokoto import hitokoto
    if word:
        return hitokoto()["hitokoto"]
    return hitokoto()


@api.get('/visitorInfo/')
async def visitor_info(ip: str = None):
    return {}


if __name__ == '__main__':
    uvicorn.run(app=api, host="127.0.0.1", port=port, log_level="info")
    # gunicorn -b 127.0.0.1: 8001 -k uvicorn.workers.UvicornWorker main: api
