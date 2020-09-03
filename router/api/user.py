from config import log, Username, Password
from fastapi import APIRouter, Form
router = APIRouter()


@router.post("/login/")
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
