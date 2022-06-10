#!/usr/bin/env python
# -*- coding: utf-8 -*-
from starlette.requests import Request
from fastapi import FastAPI, Form
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/user/login/")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):

    print('username', username)
    print('password', password)

    return templates.TemplateResponse('admin/login.html', {
        'request': request,
        'username': username,
        'password': password,
    })


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('admin/index.html', {'request': request})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000, log_level="info")
