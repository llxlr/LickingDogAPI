from settings import headers
import requests


def img():
    url = 'https://cn.bing.com'
    res = requests.get(url+'/HPImageArchive.aspx?format=js&idx=0&n=1', headers=headers)
    res.encoding = 'utf-8'
    data = res.json()
    if data:
        return {
            'img': url+data["images"][0]["url"],
            'copyright': data["images"][0]["copyright"]
        }
