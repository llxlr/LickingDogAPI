#!/usr/bin/env python
# -*- coding: utf-8 -*-
from items import NcovName
from starlette.status import HTTP_404_NOT_FOUND
from starlette.responses import JSONResponse
from fastapi import APIRouter, File, UploadFile
from config import *
import time

router = APIRouter()


@router.get('/log/', include_in_schema=False)
async def read_log():
    log.info("查看日志")
    return {'status': 200, 'data': loginfo}


@router.get('/ip/')
async def ip():
    from items.ip import ip
    return ip


@router.get('/hitokoto/')
async def hitokoto():
    from items.hitokoto import hitokoto
    data = hitokoto()
    log.info("pv,请求一次一言")
    return {
        "status": 200,
        "copyright": Copyright,
        "data": data,
        "time": time.ctime(),
    }


@router.get('/time/countdown/')
async def count_down(type):
    return ''


@router.get('/time/calendar/{type}')
async def calendar(type: str, year: str, month: str, day: str):
    from items.time import Calendar
    log.info("pv,请求一次公农历转换")
    if type in ['s2l', 'l2s']:
        return {
            "status": 200,
            "copyright": Copyright,
            "data": Calendar.solar2lunar(year, month, day) if type == 's2l' else Calendar.lunar2solar(year, month, day),
            "source": "数据源于中科院紫金山天文台",
            "time": time.ctime(),
        }


# @router.post("/files/")
# async def catvsdog_create_file(file: bytes = File(...)):
#     log.info('pv,请求一次')
#     return {"file_size": len(file)}


@router.post("/catvsdog/upload/", include_in_schema=False)
async def catvsdog_upload_image(file: UploadFile = File(...)):
    log.info('pv,上传一次猫狗图片')
    _format_ = ['image/bmp', 'image/gif', 'image/jpeg', 'image/jpg', 'image/png', 'image/x-icon']
    if file.filename != '':
        if file.content_type in _format_:
            return {
                "status": 200,
                "copyright": Copyright,
                "filename": file.filename,
                "content-type": file.content_type,
                "msg": "this is a {}, everything is ok !".format(file.content_type.split('/')[1]),
                "time": time.ctime(),
            }
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,
                            content={'msg': f'{file.filename} is not found'})


@router.get('/ncov/')
async def ncov_api(name: NcovName):
    from items.ncov import get_data
    log.info('pv,请求一次新冠肺炎数据')
    return {
        "status": 200,
        "copyright": Copyright,
        "data": get_data(name),
        "source": "数据源于丁香园",
        "time": time.ctime(),
    }


@router.get('/pcc/cf/')
async def purge_cdn_cache(zone_id: str = None,
                          email: str = None,
                          global_api_key: str = None):
    from items.cdn import cf_purge
    log.info('pv,清除一次cloudflare cdn缓存')
    data = {"status": 200,
            "copyright": Copyright,
            "success": "true",
            "msg": "purge all files successfully !",
            "description": "clear cloudflare cdn caches",
            "time": time.ctime()}
    if zone_id and email and global_api_key:
        if cf_purge(zone_id, email, global_api_key)["success"]:
            return data
    else:
        if cf_purge(cf_zone_id, cf_email, cf_global_api_key)["success"]:
            return data
