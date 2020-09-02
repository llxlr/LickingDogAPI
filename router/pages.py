from starlette.requests import Request
from . import app, templates
from config import (
    hometitle, description, Copyright, analysis, headers, log
)


@app.get("/")
async def home(request: Request):
    log.info('ts,访问一次主页')
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": hometitle,
        "keywords": "API,舔狗,舔狗API,Licking Dog API,接口,FastAPI,Awesome",
        "description": description,
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/admin/")
async def admin(request: Request):
    log.info('ts,访问一次主页')
    return templates.TemplateResponse("admin/index.html", {
        "request": request,
        "title": '后台管理 - '+hometitle,
    })


@app.get("/404/")
async def admin(request: Request):
    log.info('页面404')
    return templates.TemplateResponse("404.html", {
        "request": request,
        "title": '404 NOT FOUND',
        "keywords": "404 NOT FOUND",
        "description": "404 NOT FOUND",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/bing/")
async def bing(request: Request, type: str = None):
    import requests
    data = requests.get('https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1', headers=headers).json()
    img = {'img': 'https://cn.bing.com'+data["images"][0]["url"], 'copyright': data["images"][0]["copyright"]}
    log.info('pv,访问一次必应图片')
    return templates.TemplateResponse("img/bing.html", {
        "request": request,
        "title": "Bing每日一图",
        "img": img['img'] if data and type == 'img' else img,
    })


@app.get("/catvsdog/")
async def catvsdog(request: Request):
    log.info('ts,访问一次Cat VS Dog')
    return templates.TemplateResponse("ml/catvsdog.html", {
        "request": request,
        "title": "Cat VS Dog",
        "keywords": "猫狗大战,迁移学习,分类,图像,深度学习,机器学习",
        "description": "迁移学习实现猫狗识别",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/mnist/")
async def mnist(request: Request):
    log.info('ts,访问一次Tenserflow.js实现Mnist手写字识别')
    return templates.TemplateResponse("ml/mnist.html", {
        "request": request,
        "title": "Tenserflow.js实现Mnist手写字识别",
        "keywords": "手写字识别,深度学习,分类,图像,机器学习",
        "description": "迁移学习实现猫狗识别",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/ncov/")
async def ncov(request: Request):
    log.info('ts,访问一次2020新冠肺炎实时疫情图')
    return templates.TemplateResponse("ncov.html", {
        "request": request,
        "title": "2020新冠肺炎实时疫情图",
        "subtitle": "2020新冠肺炎实时疫情图",
    })
