from settings import headers
import requests
import json


def solar2lunar(year: int, month: int, day: int):
    url = 'http://almanac.pmo.ac.cn/cgi-bin/cx/gnlcx.pl?saveas=0'
    # headers["Referer"] = 'http://almanac.pmo.ac.cn/cx/gzn/in.htm'
    r = requests.post(url, headers=headers, data=json.dumps({'year': year, 'month': month, 'day': day}))
    # r = requests.get(, headers=headers, allow_redirects=False)
    r.encoding = 'gbk'
    return r.text


def lunar2solar(year: int, month: int, day: int):
    months = ["正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "腊月"]
    days = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
            "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
            "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]
    url = 'http://almanac.pmo.ac.cn/cx/nzg/index.htm'
    return gz(year), month, day


def gz(year: int):
    tg = "甲乙丙丁戊已庚辛壬癸"  # 天干
    dz = "子丑寅卯辰巳午未申酉戌亥"  # 地支
    return tg[(year-3) % 10-1]+dz[(year-3) % 12-1]


# print(solar2lunar(year=2020, month=1, day=1))
print(lunar2solar(year=2020, month=1, day=1))
