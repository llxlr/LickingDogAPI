from starlette.requests import Request
from main import app, templates
from fastapi import Form


@app.get("/")
async def home(request: Request):
    from settings import hometitle
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": hometitle,
    })


@app.get("/bing/")
async def bing(request: Request):
    from items.bing import img
    return templates.TemplateResponse("bing.html", {
        "request": request,
        "title": "Bing每日一图",
        "info": img,
    })


@app.post("/login/")
async def login(*, username: str = Form(...), password: str = Form(...)):
    if username and password :
        return {
            "success": "true",
            "username": username,
            "msg": "login successfully !",
        }
    return {
        "success": "false",
        "msg": "username or password is not correct !",
    }


@app.get("/start/")
async def start(request: Request):
    return templates.TemplateResponse("start.html", {
        "request": request,
        "title": "示例与说明",
    })


@app.get("/catvsdog/")
async def catvsdog(request: Request):
    return templates.TemplateResponse("catvsdog.html", {
        "request": request,
        "title": "Cat VS Dog",
    })


@app.get("/mnist/")
async def mnist(request: Request):
    return templates.TemplateResponse("mnist.html", {
        "request": request,
        "title": "Tenserflow.js实现Mnist手写字识别",
    })


@app.get("/ncov/")
async def ncov(request: Request):
    return templates.TemplateResponse("ncov.html", {
        "request": request,
        "title": "2020新冠肺炎实时疫情图",
    })
