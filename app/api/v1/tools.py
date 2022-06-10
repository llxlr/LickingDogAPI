#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from fastapi import APIRouter, File, UploadFile
from amzqr import amzqr

from plugins import NcovName
from plugins.ip import ip
from plugins.hitokoto import hitokoto
from plugins.time import Calendar
from plugins.ncov import get_data

from utils.cdn import cf_purge
from utils.spider import get

from config import *


router = APIRouter()


@router.get('/log/', include_in_schema=False)
async def read_log():
    log.info("查看日志")
    return {'status': 200, 'data': log_info}


@router.get('/ip/', include_in_schema=True)
async def ip():
    return ip


@router.get('/hitokoto/', include_in_schema=True)
async def hitokoto():
    log.info("pv,请求一次一言")
    return {
        "status": 200,
        "copyright": Copyright,
        "data": hitokoto(),
        "time": time.ctime(),
    }


@router.get('', include_in_schema=True)
async def qr():
    """
    words：二维码内容，链接或者句子
    version：二维码大小，范围为[1, 40]
    level：二维码纠错级别，范围为{L, M, Q, H}，H为最高级，默认。
    picture：自定义二维码背景图，支持格式为.jpg，.png，.bmp，.gif，默认为黑白色
    colorized：二维码背景颜色，默认为False，即黑白色
    contrast：对比度，值越高对比度越高，默认为1.0
    brightness：亮度，值越高亮度越高，默认为1.0，值常和对比度相同
    save_name：二维码名称，默认为qrcode.png
    save_dir：二维码路径，默认为程序工作路径
    """

    return {}


@router.get('/time/countdown/', include_in_schema=True)
async def count_down(type):
    return ''


@router.get('/time/calendar/{type}', include_in_schema=True)
async def calendar(type: str, year: str, month: str, day: str):
    log.info("pv,请求一次公农历转换")
    if type in ['s2l', 'l2s']:
        return {
            "status": 200,
            "copyright": Copyright,
            "data": Calendar.solar2lunar(year, month, day) if type == 's2l' else Calendar.lunar2solar(year, month, day),
            "source": "数据源于中科院紫金山天文台",
            "time": time.ctime(),
        }


# @router.post("/files/", include_in_schema=True)
# async def catvsdog_create_file(file: bytes = File(...)):
#     log.info('pv,请求一次')
#     return {"file_size": len(file)}


@router.post("/catvsdog/upload/", include_in_schema=False)
async def catvsdog_upload_image(file: UploadFile = File(...)):
    _format_ = [
        'image/bmp',
        'image/gif',
        'image/jpeg',
        'image/jpg',
        'image/png',
        'image/x-icon'
    ]
    if file.filename:
        log.info(f'pv,上传一次猫狗图片,{file.filename}')
        if file.content_type in _format_:
            return {
                'status': 200,
                'copyright': Copyright,
                'filename': file.filename,
                'content-type': file.content_type,
                'msg': 'this is a {}, everything is ok !'.format(file.content_type.split('/')[1]),
                'time': time.ctime(),
            }


@router.get('/ncov/', include_in_schema=True)
async def ncov_api(name: NcovName):
    log.info('pv,请求一次新冠肺炎数据')
    return {
        'status': 200,
        'copyright': Copyright,
        'data': get_data(name),
        'source': '数据源于丁香园',
        'time': time.ctime(),
    }


@router.get('/pcc/cf/', include_in_schema=True)
async def purge_cdn_cache(zone_id=None, email=None, global_api_key=None):
    log.info('pv,清除一次cloudflare cdn缓存')
    data = {
        'status': 200,
        'copyright': Copyright,
        'success': 'true',
        'msg': 'purge all files successfully !',
        'description': 'clear cloudflare cdn caches',
        'time': time.ctime()
    }
    if zone_id and email and global_api_key:
        if cf_purge(zone_id, email, global_api_key)['success']:
            return data
    else:
        if cf_purge(cf_zone_id, cf_email, cf_global_api_key)['success']:
            return data


@router.get('/okex/', include_in_schema=True)
async def bitcoin_quotes():
    url = f'https://www.okex.com/v2/support/info/announce/listProject?&t={str(time.time()).replace(".", "")}'
    return get(url)


if __name__ == '__main__':
    pass
