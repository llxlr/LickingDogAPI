from settings import headers
import requests
import time


class Bilibili(object):
    """"""
    def __init__(self, uid, pns, ps, url):
        super(Bilibili, self).__init__()
        self.uid, self.url, self.pns, self.ps = uid, url, pns, ps

    def bangumi(self):
        return requests.get(self.url, headers=headers).json()


pns = 1
ps = 15
uid = 166791985
ts = 1584480325628
if not pns:
    pns = 1
if not uid:
    uid = 166791985
api = 'https://api.bilibili.com/x/space/bangumi/follow/list?type=1&ps=15&vmid={}'.format(id)


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