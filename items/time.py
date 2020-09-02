"""
参数名	是否必须	默认值	说明
date	是	无	倒计时目标日期/正计时起始日期，为一个 10 位 Unix 时间戳
type	否	1	计时类型，1 为倒计时，2 为正计时
formatType	否	1	时间格式化类型：1 – 日 | 2 – 日时 | 3 – 日时分 | 4 – 日时分秒 | 5 – 年月日 | 6 – 年月日时 | 7 – 年月日时分 | 8 – 年月日时分秒
textType	否	1	时间单位类型：1 – “年月日时分秒” | 2 – “YMDhms” | 3 – “Years Months Days Hours Mins Secs”
font	否	1	字体类型 1 – 无衬线字体 | 2 – 楷体
spacing	否	3	字符之间的间距，一个整数
color	否	#000000	字体颜色，一个十六进制颜色编码
strokeColor	否	#000000	字体边框颜色，一个十六进制颜色编码
strokeWidth	否	0	字体边框宽度，一个整数
fontSize	否	25	字体大小，一个整数
left	否	空	显示在倒计时左边的文字
right	否	空	显示在倒计时右边的文字
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from config import headers
from datetime import datetime
import time


def _driver(url: str):
    """实例化driver"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument(f"user-agent='{headers['User-Agent']}'")
    wd = webdriver.Chrome(options=options)
    wd.get(url)
    return wd


def gz(year: int):
    """干支计算"""
    tg = "甲乙丙丁戊已庚辛壬癸"  # 天干
    dz = "子丑寅卯辰巳午未申酉戌亥"  # 地支
    return tg[(year-3) % 10-1]+dz[(year-3) % 12-1]


class Calendar:
    @staticmethod
    def solar2lunar(year: str, month: str, day: str):
        """公历转农历"""
        now = datetime.now().year
        if int(year) > now:
            return f'年份不能大于{now}年'
        wd = _driver('http://almanac.pmo.ac.cn/cx/gzn/in.htm')
        for key, value in {'year': year, 'month': month, 'day': day}.items():
            wd.find_element_by_xpath(f'//input[@name="{key}"]').clear()
            wd.find_element_by_xpath(f'//input[@name="{key}"]').send_keys(value)
        wd.find_element_by_xpath('//input[@type="submit"]').click()
        wd.switch_to.window(wd.window_handles[1])
        ct = [td.text.replace('\ue003', '') for td in wd.find_elements_by_xpath('//td[@align="left"]')]
        return {'农历年': ct[0], '农历日期': ct[1], '公历当月节气': f'{ct[2]}, {ct[3]}'}

    @staticmethod
    def lunar2solar(year: str, month: str, day: str):
        """农历转公历"""
        wd = _driver('http://almanac.pmo.ac.cn/cx/nzg/in.htm')
        for key, value in {'year': year, 'month': month, 'day': day}.items():
            sel = wd.find_element_by_xpath(f'//select[@id="{key}"]')
            Select(sel).select_by_value(value)
        wd.find_element_by_xpath('//input[@type="submit"]').click()
        wd.switch_to.window(wd.window_handles[1])
        ct = [td.text for td in wd.find_elements_by_xpath('//td[@align="left"]')]
        return {'公历年': ct[0], '公历日期': ct[1], '公历当月节气': f'{ct[2]}, {ct[3]}'} if ct else '农历这月没有这一天'


class Time(object):
    def __init__(self, time: str):
        self.time = time

    def ts2ymd(self):
        # 0代表时间戳timestamp
        t1 = time.time()
        t2 = time.strptime(self.time, "%Y-%m-%d %H:%M:%S")
        t3 = time.mktime(t2)
        return


if __name__ == '__main__':
    # print(Calendar.solar2lunar(year='2019', month='1', day='1'))
    # print(lunar2solar(year='2020', month='01', day='30'))
    # print(gz(2019))

    print()

    pass
# _svg = f'<svg xmlns="http://www.w3.org/2000/svg" height="36" width="735"><g>' \
#        f'<text text-anchor="start" letter-spacing="3" font-smoothing="antialiased" ' \
#        f'font-family="sans-serif,KaiTi" font-size="{}" ' \
#        f'y="30" x="0" stroke-width="{}" stroke="#00000000" fill="{}">{}{}{}</text></g></svg>'
