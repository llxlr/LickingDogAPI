from starlette.requests import Request
from .config import app, templates
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


@app.get('/start.html')
async def start(request: Request):
    log.info('ts,访问一次项目列表')
    return templates.TemplateResponse("start.html", {
        "request": request,
        "title": "项目列表",
        "keywords": "项目列表",
        "description": "项目列表",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/admin/")
async def admin(request: Request):
    log.info('ts,访问一次后台管理')
    return templates.TemplateResponse("admin/index.html", {
        "request": request,
        "title": "后台管理 - "+hometitle,
        "keywords": "后台管理",
        "description": "后台管理",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/login/")
async def admin(request: Request):
    log.info('ts,访问一次用户登录')
    return templates.TemplateResponse("admin/login.html", {
        "request": request,
        "title": "用户登录 - "+hometitle,
        "keywords": "用户登录",
        "description": "用户登录",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/404/")
async def admin(request: Request):
    log.info('页面404')
    return templates.TemplateResponse("404.html", {
        "request": request,
        "title": "404 NOT FOUND",
        "keywords": "404 NOT FOUND",
        "description": "404 NOT FOUND",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get('/limit.html')
async def limit(request: Request):
    return templates.TemplateResponse("limit.html", {
        "request": request,
    })


@app.get('/policy.html')
async def policy(request: Request):
    log.info('ts,访问一次隐私政策页')
    return templates.TemplateResponse("policy.html", {
        "request": request,
        "title": "隐私政策",
        "keywords": "隐私政策,隐私保护,宣言,声明",
        "description": "用户隐私政策页面",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/bing.html")
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


@app.get("/catvsdog.html")
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


@app.get("/mnist.html")
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


@app.get("/ncov.html")
async def ncov(request: Request):
    log.info('ts,访问一次2020新冠肺炎实时疫情图')
    return templates.TemplateResponse("ncov.html", {
        "request": request,
        "title": "2020新冠肺炎实时疫情图",
        "subtitle": "2020新冠肺炎实时疫情图",
    })
