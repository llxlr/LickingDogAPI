from settings import headers
from lxml import etree
import requests


def img():
    url = 'https://cn.bing.com'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    html = etree.HTML(res.text)
    link = html.xpath('//link[@id="bgLink"]/@href')
    title = html.xpath('//a[@id="sh_cp"]/@title')
    if link:
        return {
            'img': url+link[0].replace('&rf=LaDigue_1920x1080.jpg&pid=hp', ''),
            'title': title[0]
        }
