from settings import Username, Password
from fastapi import Form
from settings import log
from .api import app


@app.post("/login/")
async def login(*, username: str = Form(...), password: str = Form(...)):
    if username == Username and password == Password:
        log.info('ts,登录成功')
        return {
            "success": "true",
            "username": username,
            "msg": "login successfully !",
        }
    log.info('登录失败')
    return {
        "success": "false",
        "msg": "username or password is not correct !",
    }
