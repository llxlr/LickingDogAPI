from starlette.middleware.cors import CORSMiddleware  # Cross-Origin Resource Sharing
from starlette.templating import Jinja2Templates  # Templates
from starlette.staticfiles import StaticFiles  # Static
from fastapi.openapi.utils import get_openapi  # custom openapi
from fastapi import FastAPI
from utils.log import Logger
import settings
import os

app = FastAPI(
    title=settings.hometitle,
    description=settings.description,
    version=settings.docv,
    openapi_url=settings.version+"/openapi.json",
    docs_url=settings.version+"/docs/",
    redoc_url=None
)
origins = [
    f"http://{settings.domain}",
    f"https://{settings.domain}",
    "http://localhost",
    f"http://localhost:{settings.port}"
]


def _openapi_schema_custom():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.hometitle,
        version=settings.docv,
        description=settings.description,
        routes=app.routes
    )
    openapi_schema["info"]["x-logo"] = {"url": "https://img.white-album.top/i/2020/02/08/f7dpek.jpg"}
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = _openapi_schema_custom
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static", packages=[]), name="static")  # 静态资源设置
templates = Jinja2Templates(directory="templates")  # 页面模板

os.makedirs('cache', exist_ok=True)
log = Logger('cache/info.log')  # 设置一个日志记录器
