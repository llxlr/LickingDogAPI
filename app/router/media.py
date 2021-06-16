#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://fastapi.tiangolo.com/zh/advanced/custom-response/
https://www.runoob.com/http/http-content-type.html
"""
from fastapi.responses import FileResponse
from fastapi import Response
from router.generate import app, templates
from config import *


@app.get('/favicon.ico', include_in_schema=False)
async def favicon_config():
    return FileResponse(path=f'{path}/static/favicon.ico', media_type='image/x-icon')


@app.get('/config.js', include_in_schema=False)
async def docsify_config():
    return Response(content=templates.get_template(name='config.tmpl').render(
        start_time=start_time,
        analysis=analysis
    ), media_type='application/javascript; charset=utf-8')


@app.get('/sw.js', include_in_schema=False)
async def swjs():
    return FileResponse(path=f'{path}/static/js/sw.js', media_type='application/javascript; charset=utf-8')


@app.get('/robots.txt', include_in_schema=False)
async def docsify_config():
    return Response(content=templates.get_template(name='robots.txt').render(
    ), media_type='text/plain; charset=utf-8')


@app.get('/LICENSE', include_in_schema=False)
async def license_():
    return FileResponse(path=f'{path}/LICENSE', media_type='text/plain; charset=utf-8')


@app.get('/README.md', include_in_schema=False)
async def readme_():
    return FileResponse(path=f'{path}/README.md', media_type='text/markdown; charset=utf-8')


@app.get('/_coverpage.md', include_in_schema=False)
async def docsify_config():
    return Response(content=templates.get_template(name='docs/_coverpage.md').render(
        title=title,
        version=version,
        description=description,
        domain=f"https://{master}.{suffix}/",
        docs_domain=f"https://{domain}/v1/docs/",
    ), media_type='text/markdown; charset=utf-8')


@app.get('/_sidebar.md', include_in_schema=False)
async def docsify_config():
    return Response(content=templates.get_template(name='docs/_sidebar.md').render(
    ), media_type='text/markdown; charset=utf-8')


@app.get('/_navbar.md', include_in_schema=False)
async def docsify_config():
    return Response(content=templates.get_template(name='docs/_navbar.md').render(
    ), media_type='text/markdown; charset=utf-8')


@app.get('/_404.md', include_in_schema=False)
async def _404():
    return Response(content=templates.get_template(name='docs/_404.md').render(
    ), media_type='text/markdown; charset=utf-8')


@app.get('/about.md', include_in_schema=False)
async def about():
    return Response(content=templates.get_template(name='docs/about.md').render(
    ), media_type='text/markdown; charset=utf-8')


@app.get('/guide.md', include_in_schema=False)
async def guide():
    return Response(content=templates.get_template(name='docs/guide.md').render(
    ), media_type='text/markdown; charset=utf-8')


@app.get('/home.md', include_in_schema=False)
async def home():
    return Response(content=templates.get_template(name='docs/home.md').render(
    ), media_type='text/markdown; charset=utf-8')


@app.get("/items/catvsdog.md", include_in_schema=False)
async def catvsdog():
    log.info('ts,访问一次Cat VS Dog')
    return Response(templates.get_template(name='docs/items/catvsdog.md').render(
        title="Cat VS Dog",
        description="迁移学习实现猫狗识别",
    ), media_type='text/markdown; charset=utf-8')


@app.get("/items/mnist.md", include_in_schema=False)
async def mnist():
    log.info('ts,访问一次Tenserflow.js实现Mnist手写字识别')
    return Response(templates.get_template(name='docs/items/mnist.md').render(
        title="Tenserflow.js实现Mnist手写字识别",
        description="迁移学习实现猫狗识别",
    ), media_type='text/markdown; charset=utf-8')


@app.get('/countdown.svg', include_in_schema=False)
async def favicon_config(year=None,
                         color=None,
                         font_size=None,
                         font_family=None):
    return Response(templates.get_template(name='docs/items/countdown.svg').render(
        year=year,
        date=None,
        color=color if color else '#5e72e4',
        font_size=font_size if font_size else '30',
        font_family=font_family if font_family else 'sans-serif,KaiTi',
    ), media_type='text/xml; charset=utf-8')


@app.get('/poem.svg', include_in_schema=False)
async def favicon_config(color=None,
                         font_size=None,
                         font_family=None,
                         content=None):
    return Response(templates.get_template(name='docs/items/poem.svg').render(
        color=color if color else '#5e72e4',
        font_size=font_size if font_size else '30',
        font_family=font_family if font_family else 'KaiTi,Segoe UI,Lucida Grande,Helvetica,Arial,Microsoft YaHei,'
                                                    'FreeSans,Arimo,Droid Sans,wenquanyi micro hei,Hiragino Sans GB,'
                                                    'Hiragino Sans GB W3,sans-serif',
        content=content,
    ), media_type='text/xml; charset=utf-8')
