from items import Charts, Music, NcovName
from starlette.status import HTTP_404_NOT_FOUND
from starlette.responses import JSONResponse
from fastapi import File, UploadFile
from .pages import app
import time
from settings import (
    log, version, Copyright,
    cf_zone_id, cf_email, cf_global_api_key
)


@app.get('/log/')
async def read_log():
    from utils.log import read_log
    return read_log()


@app.get(version+'/ip/')
async def ip():
    from items.ip import ip
    return ip


@app.get(version+'/hitokoto/')
async def hitokoto():
    from items.hitokoto import hitokoto
    data = hitokoto()
    log.info("pv,请求一次一言")
    return {
        "code": 200,
        "copyright": Copyright,
        "data": data,
        "time": time.ctime(),
    }


@app.get(version+'/calendars/{type}')
def calendar(type: str, year: str, month: str, day: str):
    from items.calendars import lunar2solar, solar2lunar
    log.info("pv,请求一次公农历转换")
    if type in ['s2l', 'l2s']:
        return {
            "code": 200,
            "Copyright": Copyright,
            "data": solar2lunar(year, month, day) if type == 's2l' else lunar2solar(year, month, day),
            "source": "数据源于中科院紫金山天文台",
            "time": time.ctime(),
        }


@app.get(version+"/github/")
async def github_trending(type: str = "trending",
                          date: str = "daily",
                          spoken_lang: str = None,
                          language: str = None):
    from items.github import Github
    log.info("pv,请求一次Github Trending")
    if type in ['trending', 'developers']:
        return {
            "code": 200,
            "Copyright": Copyright,
            "data": Github(type, date, None, language).trending if type == 'trending'
            else Github(type, date, spoken_lang, language).developers,
            "time": time.ctime(),
        }


@app.get(version+"/music/{name}")
async def music(name: Music.Service, type: Music.Type, id: int):
    if name == Music.Service.cloudmusic:
        log.info('pv,请求一次网易云音乐api')
        from items.music import CloudMusic, music_type
        return {
            "code": 200,
            "copyright": Copyright,
            "data": music_type(CloudMusic, type, id),
            "time": time.ctime(),
        }
    elif name == Music.Service.qq:
        log.info('pv,请求一次QQ音乐api')
        from items.music import QQ, music_type
        return {
            "code": 200,
            "copyright": Copyright,
            "data": music_type(QQ, type, id),
            "time": time.ctime(),
        }
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND, content=name)


@app.get(version+"/billboard/{chart}")
async def billboard(chart: Charts):
    from items.billboard import get_content
    log.info('pv,请求一次公告牌数据')
    if chart in (Charts.hot100, Charts.billboard200,
                 Charts.artist100, Charts.social50):
        return {
            "code": 200,
            "copyright": Copyright,
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


@app.post(version+"/catvsdog/upload/")
async def catvsdog_upload_image(file: UploadFile = File(...)):
    log.info('pv,上传一次猫狗图片')
    _format_ = ['image/bmp', 'image/gif', 'image/jpeg', 'image/jpg', 'image/png', 'image/x-icon']
    if file.filename != '':
        if file.content_type in _format_:
            return {
                "code": 200,
                "Copyright": Copyright,
                "filename": file.filename,
                "content-type": file.content_type,
                "msg": "this is a {}, everything is ok !".format(file.content_type.split('/')[1]),
                "time": time.ctime(),
            }
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,
                            content={'msg': f'{file.filename} is not found'})


@app.get(version+"/ncov/")
async def ncov_api(name: NcovName):
    from items.ncov import get_data
    log.info('pv,请求一次新冠肺炎数据')
    return {
        "code": 200,
        "copyright": Copyright,
        "data": get_data(name),
        "source": "数据源于丁香园",
        "time": time.ctime(),
    }


@app.get('/pcc/')
async def purge_cdn_cache(zone_id: str = None, email: str = None, global_api_key: str = None):
    import requests
    if (zone_id is None) and (email is None) and (global_api_key is None):
        zone_id, email, global_api_key = cf_zone_id, cf_email, cf_global_api_key
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
    headers = {
        "X-Auth-Email": f"{email}",
        "X-Auth-Key": f"{global_api_key}",
        "Content-Type": "application/json"
    }
    post_data = '{"purge_everything": true}'
    res = requests.post(url, post_data, headers=headers).json()
    log.info('pv,清除一次cloudflare cdn缓存')
    if res["success"]:
        return {
            "code": 200,
            "copyright": Copyright,
            "success": "true",
            "msg": "purge everything successfully !",
            "description": "clear cloudflare cdn caches",
            "time": time.ctime(),
        }


# @app.get('/visitorInfo/')
# async def visitor_info(ip: str = None):
#     log.info('请求一次')
#     return {}
