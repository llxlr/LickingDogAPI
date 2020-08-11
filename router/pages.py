from starlette.requests import Request
from . import app, templates, log


@app.get("/")
async def home(request: Request):
    from settings import hometitle
    log.info('ts,访问一次主页')
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": hometitle,
    })


@app.get("/bing/")
async def bing(request: Request):
    from items.bing import img
    img = img()
    log.info('pv,访问一次必应图片')
    return templates.TemplateResponse("bing.html", {
        "request": request,
        "title": "Bing每日一图",
        "img": img['img'],
    })


@app.get("/start/")
async def start(request: Request):
    log.info('ts,访问一次示例与说明')
    return templates.TemplateResponse("start.html", {
        "request": request,
        "title": "示例与说明",
    })


@app.get("/catvsdog/")
async def catvsdog(request: Request):
    log.info('ts,访问一次Cat VS Dog')
    return templates.TemplateResponse("catvsdog.html", {
        "request": request,
        "title": "Cat VS Dog",
    })


@app.get("/mnist/")
async def mnist(request: Request):
    log.info('ts,访问一次Tenserflow.js实现Mnist手写字识别')
    return templates.TemplateResponse("mnist.html", {
        "request": request,
        "title": "Tenserflow.js实现Mnist手写字识别",
    })


@app.get("/ncov/")
async def ncov(request: Request):
    log.info('ts,访问一次2020新冠肺炎实时疫情图')
    return templates.TemplateResponse("ncov.html", {
        "request": request,
        "title": "2020新冠肺炎实时疫情图",
        "subtitle": "2020新冠肺炎实时疫情图",
    })
