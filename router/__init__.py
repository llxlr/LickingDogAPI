from starlette.middleware.cors import CORSMiddleware  # Cross-Origin Resource Sharing
from starlette.templating import Jinja2Templates  # Templates
from starlette.staticfiles import StaticFiles  # Static
from fastapi.openapi.utils import get_openapi  # custom openapi
from fastapi import FastAPI
import settings

app = FastAPI(
    title=settings.hometitle,
    description=settings.description,
    version=settings.docv,
    openapi_url=settings.version+"/openapi.json",
    docs_url=settings.version+"/docs/",
    redoc_url=None
)
domain = settings.domain.split('.')
origins = [
    f"http://{domain[0]}.{domain[1]}",
    f"https://{domain[0]}.{domain[1]}",
    
    "http://localhost",
    f"http://localhost:{settings.port}",
    "https://localhost",
    f"https://localhost:{settings.port}",
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
    openapi_schema["info"]["x-logo"] = {"url": "https://cdn.jsdelivr.net/gh/jamesyangget/cdn@img/2020/02/08/f7dpek.jpg"}
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = _openapi_schema_custom
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许跨域请求的域名列表
    allow_origin_regex=r'https?://.*\.{}\.{}'.format(domain[0], domain[1]),  # 允许跨域请求的域名正则表达式
    allow_credentials=True,  # 在跨域请求时是否支持cookie
    allow_methods=["*"],  # 允许跨域请求的HTTP方法列表
    allow_headers=["*"],  # 跨域请求支持的HTTP头信息列表
    expose_headers=[],  # 对浏览器可见的返回结果头信息，默认为[]
    max_age=60,  # 浏览器缓存CORS返回结果的最大时长，默认为600(单位秒)
)
app.mount("/static", StaticFiles(directory="static", packages=[]), name="static")  # 静态资源设置
templates = Jinja2Templates(directory="templates")  # 页面模板
