from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from settings import headers
from datetime import datetime


def driver(url: str):
    """实例化driver"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument(f"user-agent='{headers['User-Agent']}'")
    wd = webdriver.Chrome(options=options)
    wd.get(url)
    return wd


def solar2lunar(year: str, month: str, day: str):
    """公历转农历"""
    now = datetime.now().year
    if int(year) > now:
        return f'年份不能大于{now}年'
    wd = driver('http://almanac.pmo.ac.cn/cx/gzn/in.htm')
    for key, value in {'year': year, 'month': month, 'day': day}.items():
        wd.find_element_by_xpath(f'//input[@name="{key}"]').clear()
        wd.find_element_by_xpath(f'//input[@name="{key}"]').send_keys(value)
    wd.find_element_by_xpath('//input[@type="submit"]').click()
    wd.switch_to.window(wd.window_handles[1])
    ct = [td.text.replace('\ue003', '') for td in wd.find_elements_by_xpath('//td[@align="left"]')]
    return {'农历年': ct[0], '农历日期': ct[1], '公历当月节气': f'{ct[2]}, {ct[3]}'}


def lunar2solar(year: str, month: str, day: str):
    """农历转公历"""
    wd = driver('http://almanac.pmo.ac.cn/cx/nzg/in.htm')
    for key, value in {'year': year, 'month': month, 'day': day}.items():
        sel = wd.find_element_by_xpath(f'//select[@id="{key}"]')
        Select(sel).select_by_value(value)
    wd.find_element_by_xpath('//input[@type="submit"]').click()
    wd.switch_to.window(wd.window_handles[1])
    ct = [td.text for td in wd.find_elements_by_xpath('//td[@align="left"]')]
    return {'公历年': ct[0], '公历日期': ct[1], '公历当月节气': f'{ct[2]}, {ct[3]}'} if ct else '农历这月没有这一天'


def gz(year: int):
    """干支计算"""
    tg = "甲乙丙丁戊已庚辛壬癸"  # 天干
    dz = "子丑寅卯辰巳午未申酉戌亥"  # 地支
    return tg[(year-3) % 10-1]+dz[(year-3) % 12-1]


if __name__ == '__main__':
    print(solar2lunar(year='2019', month='1', day='1'))
    # print(lunar2solar(year='2020', month='01', day='30'))
    # print(gz(2019))
    pass
