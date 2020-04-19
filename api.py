from items import Charts, Music
from starlette.status import HTTP_404_NOT_FOUND
from starlette.responses import JSONResponse
from fastapi import File, UploadFile
from page import app
import settings
import time


@app.get(settings.version+'/hitokoto/')
async def hitokoto():
    from items.hitokoto import hitokoto
    data = hitokoto()
    return {
        "code": 200,
        "copyright": settings.Copyright,
        "data": data,
        "time": time.ctime(),
    }


@app.get(settings.version+"/github/")
async def github_trending(type: str = "trending",
                          date: str = "daily",
                          spoken_lang: str = None,
                          language: str = None):
    from items.github import Github
    if type != "trending":
        return {
            "code": 200,
            "Copyright": settings.Copyright,
            "data": Github(type, date, None, language).developers,
            "time": time.ctime(),
        }
    return {
        "code": 200,
        "Copyright": settings.Copyright,
        "data": Github(type, date, spoken_lang, language).trending,
        "time": time.ctime(),
    }


@app.get(settings.version+"/music/{name}")
async def music(name: Music.Service, type: Music.Type, id: int):
    if name == Music.Service.cloudmusic:
        from items.music import CloudMusic, music_type
        return {
            "code": 200,
            "copyright": settings.Copyright,
            "data": music_type(CloudMusic, type, id),
            "time": time.ctime(),
        }
    elif name == Music.Service.qq:
        from items.music import QQ, music_type
        return {
            "code": 200,
            "copyright": settings.Copyright,
            "data": music_type(QQ, type, id),
            "time": time.ctime(),
        }
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND, content=name)


@app.get(settings.version+"/billboard/{chart}")
async def billboard(chart: Charts):
    from items.billboard import get_content
    if chart in (Charts.hot100, Charts.billboard200,
                 Charts.artist100, Charts.social50):
        return {
            "code": 200,
            "copyright": settings.Copyright,
            "data": get_content(chart),
            "time": time.ctime(),
        }
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,
                            content={'msg': f'{chart} is not found'})


# @app.post(version+"/files/")
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
                "time": time.ctime(),
            }
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,
                            content={'msg': f'{file.filename} is not found'})


@app.get(settings.version+"/ncov/")
async def ncov_api(name: str):
    from items.ncov import get_data
    return {
        "code": 200,
        "copyright": settings.Copyright,
        "data": get_data(name),
        "time": time.ctime(),
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
            "time": time.ctime(),
        }


# @app.get('/visitorInfo/')
# async def visitor_info(ip: str = None):
#     return {}
