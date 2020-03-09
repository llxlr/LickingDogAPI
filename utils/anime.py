import requests
import time
from functools import wraps

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.130 Safari/537.36 Edg/79.0.309.71'
}


class Bilibili(object):
    """"""
    def __init__(self, id, url):
        super(Bilibili, self).__init__()
        self.id, self.url = id, url

    def bangumi(self):
        r = requests.get(self.url, headers=headers)


class Bangumi(object):
    """"""
    def __init__(self, id):
        super(Bangumi, self).__init__()
        self.id = id


id = 166791985
api = 'https://api.bilibili.com/x/space/bangumi/follow/list?type=1&ps=15&vmid={}'.format(id)

# for i in r.json()['data']['list']:
# 	data = [
#         "https://www.bilibili.com/bangumi/play/ss{}/".format(i['season_id'])
#     ]
# 	print(data)
# print(r.json())

'''

{
'season_id': 28320, 
'season_type_name': '番剧', 
'title': '命运-冠位指定 绝对魔兽战线 巴比伦尼亚', 
'cover': 'http://i0.hdslb.com/bfs/bangumi/12cae87721deeee6cda923e49b6a7c1e9e81cfb8.png', 
'new_ep': {
    'id': 285893, 
    'index_show': '更新至第6节', 
    'cover': 'http://i0.hdslb.com/bfs/archive/2d04c171bd204e6ea33b3dd4563bc03c4f988a36.jpg', 
    'title': '第6节', 
    'long_title': '天命泥板', 
    'pub_time': '2019-11-10 00:00:03'
    }, 
'evaluate': '人理续存保障机构·迦勒底，对于仅凭魔术无法看见的世界，仅凭科学无法计算的世界进行观测，为了让已被证明会灭亡于2017年的人类史存续下去，日夜持续着活动。\n人类灭亡的原因，是在历史上数个地点突然出现的“...', 
'areas': [{'id': 2, 'name': '日本'}]
}

'''


def test(func):
    cache = {}

    @wraps(func)
    def test_func(*args, **kwargs):
        # 函数的名称作为key
        key, result = func.__name__, None
        # 判断是否存在缓存
        if key in cache.keys():
            (result, updateTime) = cache[key]
            # 过期时间固定为5秒
            if time.time() - updateTime < 5:
                print("5s后可调用函数", key)
                result = updateTime
            else:
                print("缓存过期，函数", key, "可调用")
                result = None
        else:
            print("函数", key, "无缓存")
        # 如果过期，或则没有缓存调用方法
        if result is None:
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
        return result
    return test_func


@test
def a(x):
    print('调用函数', a.__name__)


if __name__ == '__main__':
    a(1)
