from settings import headers, PIXIV_EMAIL, PIXIV_PASSWD
from lxml import etree
import requests
import http.cookiejar as cj
import re
import os

main_url = "https://www.pixiv.net"
login_url = 'https://accounts.pixiv.net/login'  # 登陆的URL
post_url = 'https://accounts.pixiv.net/api/login?lang=en'  # 提交POST请求的URL
cache = '../cache/'
os.makedirs(cache, exist_ok=True)

params = {
    'lang': 'en',
    'source': 'pc',
    'view_type': 'page',
    'ref': 'wwwtop_accounts_index'
}  # get提交参数
# post提交参数
data = {
    'pixiv_id': PIXIV_EMAIL,
    'password': PIXIV_PASSWD,
    'captcha': '',
    'g_reaptcha_response': '',
    'post_key': '',
    'source': 'pc',
    'ref': 'wwwtop_accounts_indes',
    'return_to': main_url
}
xps = [
    '',
    '',
    '',
    '',
    '',
]


def load_cookie():
    """载入本地cookie"""
    s = requests.session()
    s.cookies = cj.LWPCookieJar(filename=cache+'cookies')
    s.cookies.load(filename='cookies', ignore_discard=True)


def cookie2dict(cookie):
    """cookie转成字典"""
    cookie_dict = {}
    items = cookie.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        cookie_dict[key] = value
    return cookie_dict


def login():
    """Session模拟登录"""
    with requests.Session() as s:
        s.cookies = cj.LWPCookieJar()  # 接入容器
        res = s.get(login_url, headers=headers, params=params)  # 获取登录页面
        key = re.findall(r'name="post_key" value="(.*?)">', res.text)  # 获取post_key
        data['post_key'] = key[0]
        result = s.post(post_url, data=data)  # 模拟登录
        s.cookies.save(
            filename=cache+'cookies',
            ignore_discard=True,
            ignore_expires=True
        )  # 保存cookie到本地，忽略关闭浏览器丢失，忽略失效
    return result.json()  # 返回json信息


if __name__ == "__main__":
    __doc__ = """
    Cookie，有时也用其复数形式 Cookies，指某些网站为了辨别用户身份、进行 session 跟踪而储存在用户本
    地终端上的数据（通常经过加密）。定义于 RFC2109 和 2965 中的都已废弃，最新取代的规范是 RFC6265。

    Session:在计算机中，尤其是在网络应用中，称为“会话控制”。Session对象存储特定用户会话所需的属性及配
    置信息。这样，当用户在应用程序的Web页之间跳转时，存储在Session对象中的变量将不会丢失，而是在整个用
    户会话中一直存在下去。当用户请求来自应用程序的 Web 页时，如果该用户还没有会话，则 Web 服务器将自动
    创建一个Session对象。当会话过期或被放弃后，服务器将终止该会话。Session 对象最常见的一个用法就是存
    储用户的首选项。例如，如果用户指明不喜欢查看图形，就可以将该信息存储在 Session 对象中。有关使用Session
    对象的详细信息，请参阅“ASP 应用程序”部分的“管理会话”。注意 会话状态仅在支持cookie的浏览器中保留。

    无论cookies如何加密，我们只要获取到它就可以，利用cookies实现我们得模拟登陆即可。
    """

    # # Cookies 登录 start
    # with open('../../tmp/rawcookies.txt', 'r', encoding='utf-8') as f:
    #     rawcookies = f.read()
    # r = requests.get(url_main, headers=headers, cookies=cookie2dict(rawcookies))
    # print(r.status_code)
    # print(r.text)
    # # end

    # Session 模拟登录 start
    print(login())
    # end
    pass
