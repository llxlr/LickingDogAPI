#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import log
import requests
import yagmail


class Email(object):
    def __init__(self, username, password, host):
        self.yag = yagmail.SMTP(user=username, password=password, host=host)

    def send(self, user, title, contents):
        self.yag.send(to=user, subject=title, contents=contents)


class Server(object):
    def __init__(self, sckey, title, contents):
        self.SCKEY, self.title, self.contents = sckey, title, contents

    def send(self):
        r = requests.get(f'https://sc.ftqq.com/{self.SCKEY}.send?text={self.title}&desp={self.contents}')
        log.info("server酱发送消息成功！") if r.status_code == 200 else log.error("server酱发送消息失败！")
