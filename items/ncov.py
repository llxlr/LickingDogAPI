from settings import headers
import requests
import time
import json
import os
import re

url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
# regex
regex = [
    r'window.getAreaStat = (.*?)}catch',  # China
    r'window.getListByCountryTypeService2true = (.*?)}catch',  # World
    r'window.getTimelineService1 = (.*?)}catch',  # China News
    r'window.getTimelineService2 = (.*?)}catch',  # World News
]
patterns = list(map(re.compile, regex))


def date(t):
    t = time.localtime(t)
    return f"{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}"


def save_cache(status=False):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    cache_path, f_name, text = '../cache', 'ncov.html', ''
    if status:
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(r.text)
    else:
        f_name = cache_path+'/'+f_name if os.path.exists(cache_path) else os.makedirs(cache_path, exist_ok=True)
        if not os.path.exists(f_name):
            with open(f_name, 'w', encoding='utf-8') as f:
                f.write(r.text)
        with open(f_name, 'r', encoding='utf-8') as f:
            return f.read()


def get_data(type_):
    if time.localtime().tm_min in [0, 30]:
        save_cache(status=True)
    text, data = save_cache(), []
    for idx, dt in enumerate(filter(lambda y: y != [], map(lambda x: x.findall(text), patterns))):
        cc, c, suspected, cured, dead, overseas = 0, 0, 0, 0, 0, 0  # 现存确诊数,疑似,治愈数,死亡数,境外输入
        if (type_ == 'china') and (idx == 0):
            data = []
            for i in json.loads(dt[0]):
                cc += i["currentConfirmedCount"]
                c += i["confirmedCount"]
                suspected += i["suspectedCount"]
                dead += i["deadCount"]
                cured += i["curedCount"]
                j = list(filter(lambda x: x["cityName"] == "境外输入", i["cities"]))
                overseas += j[0]["currentConfirmedCount"] if j else 0
                data.append({"name": i["provinceShortName"], "value": i["currentConfirmedCount"]})
            return {"currentConfirmed": cc, "Confirmed": c, "suspected": suspected, "cured": cured,
                    "dead": dead, "overseas": overseas, "data": data}
        elif (type_ == 'world') and (idx == 1):
            data = []
            for i in json.loads(dt[0]):
                cc += i["currentConfirmedCount"]
                c += i["confirmedCount"]
                cured += i["curedCount"]
                dead += i["deadCount"]
                data.append({"name": i["countryFullName"],
                             "value": i["currentConfirmedCount"],
                             "provinceName": i["provinceName"]})
            return {"currentConfirmed": cc, "Confirmed": c, "dead": dead, "data": data}
        elif ((type_ == 'cnews') and (idx == 2)) or ((type_ == 'wnews') and (idx == 3)):
            data = []
            for i in json.loads(dt[0]):
                data.append({"date": date(i["pubDate"]/1000), "datestr": i["pubDateStr"], "title": i["title"],
                             "summary": i["summary"], "source": i["infoSource"], "url": i["sourceUrl"]})
            return data


if __name__ == '__main__':
    print(get_data('china'))
