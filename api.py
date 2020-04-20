from items import Charts, Music, NcovName
from starlette.status import HTTP_404_NOT_FOUND
from starlette.responses import JSONResponse
from fastapi import File, UploadFile
from page import app, log
import settings
import time


@app.get(settings.version+'/hitokoto/')
async def hitokoto():
    from items.hitokoto import hitokoto
    data = hitokoto()
    log.info("pv,请求一次一言")
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
    log.info("pv,请求一次Github Trending")
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
        log.info('pv,请求一次网易云音乐api')
        from items.music import CloudMusic, music_type
        return {
            "code": 200,
            "copyright": settings.Copyright,
            "data": music_type(CloudMusic, type, id),
            "time": time.ctime(),
        }
    elif name == Music.Service.qq:
        log.info('pv,请求一次QQ音乐api')
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
    log.info('pv,请求一次公告牌数据')
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
#     log.info('pv,请求一次')
#     return {"file_size": len(file)}


@app.post(settings.version+"/catvsdog/upload/")
async def catvsdog_upload_image(file: UploadFile = File(...)):
    log.info('pv,上次一次猫狗图片')
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
async def ncov_api(name: NcovName):
    from items.ncov import get_data
    log.info('pv,请求一次新冠肺炎数据')
    return {
        "code": 200,
        "copyright": settings.Copyright,
        "data": get_data(name),
        "source": "数据源于丁香园",
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
    log.info('pv,清除一次cloudflare cdn缓存')
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
#     log.info('请求一次')
#     return {}
