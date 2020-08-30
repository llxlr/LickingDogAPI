from starlette.requests import Request
from . import app, templates
from settings import hometitle, log


@app.get("/")
async def home(request: Request):
    log.info('ts,访问一次主页')
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": hometitle,
    })


@app.get("/admin/")
async def admin(request: Request):
    log.info('ts,访问一次主页')
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": '后台管理 - '+hometitle,
    })


@app.get("/bing/")
async def bing(request: Request):
    from items.bing import img
    img = img()
    log.info('pv,访问一次必应图片')
    return templates.TemplateResponse("img/bing.html", {
        "request": request,
        "title": "Bing每日一图",
        "img": img['img'],
    })


@app.get("/catvsdog/")
async def catvsdog(request: Request):
    log.info('ts,访问一次Cat VS Dog')
    return templates.TemplateResponse("ml/catvsdog.html", {
        "request": request,
        "title": "Cat VS Dog",
    })


@app.get("/mnist/")
async def mnist(request: Request):
    log.info('ts,访问一次Tenserflow.js实现Mnist手写字识别')
    return templates.TemplateResponse("ml/mnist.html", {
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
