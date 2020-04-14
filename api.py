from starlette.status import HTTP_404_NOT_FOUND
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi import Form, File, UploadFile
from enum import Enum
from main import app, templates
import settings


@app.get("/")
async def home(request: Request):
    from settings import hometitle
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": hometitle,
    })


@app.get("/bing/")
async def bing(request: Request):
    from items.bing import img
    return templates.TemplateResponse("bing.html", {
        "request": request,
        "title": "Bing每日一图",
        "info": img,
    })


@app.post("/login/")
async def login(*, username: str = Form(...), password: str = Form(...)):
    if username and password :
        return {
            "success": "true",
            "username": username,
            "msg": "login successfully !",
        }
    return {
        "success": "false",
        "msg": "username or password is not correct !",
    }


@app.get("/start/")
async def start(request: Request):
    return templates.TemplateResponse("start.html", {
        "request": request,
        "title": "示例与说明",
    })


@app.get("/catvsdog/")
async def catvsdog(request: Request):
    return templates.TemplateResponse("catvsdog.html", {
        "request": request,
        "title": "Cat VS Dog",
    })


@app.get("/mnist/")
async def mnist(request: Request):
    return templates.TemplateResponse("mnist.html", {
        "request": request,
        "title": "Tenserflow.js实现Mnist手写字识别",
    })


@app.get("/ncov/")
async def ncov(request: Request):
    from items.ncov import get_data
    return templates.TemplateResponse("ncov.html", {
        "request": request,
        "title": "2020新冠肺炎实时疫情图",
        "data1": get_data('china')["data"],
        "data2": get_data('world')["data"],
        # "news1": get_data('cnews'),
        # "news2": get_data('wnews'),
    })


@app.get(settings.version+'/hitokoto/')
async def hitokoto():
    from items.hitokoto import hitokoto
    data = hitokoto()
    return {
        "code": 200,
        "copyright": settings.Copyright,
        "data": data["hitokoto"]
    }


@app.get(settings.version+"/github/")
async def github_trending(type_: str = "trending", date: str = "daily", spoken_lang: str = None, language: str = None):
    from items.github import Github
    if type_ != "trending":
        return {
            "code": 200,
            "Copyright": settings.Copyright,
            "data": Github("developers", language, date).developers
        }
    return {
        "code": 200,
        "Copyright": settings.Copyright,
        "data": Github(type_, spoken_lang, language, date).trending
    }


@app.get(settings.version+"/music/{name}")
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


# @api.get(version+"/billboard/{chart}")
# async def billboard(chart: str):
#     from items.billboard import get_content
#
#     class Charts(Enum):
#         hot100: str = 'hot-100'
#         billboard200: str = 'billboard-200'
#         artist100: str = 'artist-100'
#         social50: str = 'social-50'
#
#     if chart in [Charts.hot100,
#                  Charts.billboard200,
#                  Charts.artist100,
#                  Charts.social50]:
#         return get_content(chart)
#     else:
#         return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={'msg': f'{chart} is not found'})


# @api.post(version+"/files/")
# async def catvsdog_create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}


@app.post(settings.version+"/catvsdog/upload/")
async def catvsdog_upload_image(file: UploadFile = File(...)):
    _format_ = ['image/bmp', 'image/gif', 'image/jpeg', 'image/jpg', 'image/png', 'image/x-icon']
    if file.filename != '':
        if file.content_type in _format_:
            return {
                "code": 200,
                "Copyright": settings.Copyright,
                "filename": file.filename,
                "content-type": file.content_type,
                "msg": "this is a {}, everything is ok !".format(file.content_type.split('/')[1]),
            }
    # text = await file.read()
    # await file.close()
    # return {
    #     "filename": file.filename,
    #     "content-type": file.content_type,
    #     "msg": "this is a {} file !".format(file_type[1]),
    #     "content": text,
    # }


@app.get(settings.version+"/ncov/")
async def ncov_api(name: str):
    from items.ncov import get_data
    return {
        "code": 200,
        "copyright": settings.Copyright,
        "data": get_data(name)
    }


@app.get('/purge-cdn-cache/')
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
            "copyright": settings.Copyright,
            "success": "true",
            "msg": "purge everything successfully !",
            "description": "clear cloudflare cdn caches",
        }


@app.get('/visitorInfo/')
async def visitor_info(ip: str = None):
    return {}
