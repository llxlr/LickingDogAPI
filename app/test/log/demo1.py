#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging


class LoggerV1:
    def __init__(self, path, clevel=logging.DEBUG, flevel=logging.DEBUG):
        self.path = path
        self.logger = logging.getLogger(self.path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # 设置文件日志
        fh = logging.FileHandler(self.path, encoding='utf-8')
        fh.setFormatter(fmt)
        fh.setLevel(flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def criti(self, message):
        self.logger.critical(message)

    def read_log(self):
        """读取日志信息,pv:调用数,uv:用户数,ts:浏览量"""
        pv, uv, ts = 0, 0, 0
        with open(self.path, 'r', encoding='utf-8') as f:
            for i in f.readlines():
                if 'pv' in i:
                    pv += 1
                elif 'uv' in i:
                    uv += 1
                elif 'ts' in i:
                    ts += 1
            return {'pv': pv, 'uv': uv, 'ts': ts}


if __name__ == '__main__':
    import os
    path = f'{os.path.dirname(__file__)}/../../cache/'
    # log1 = LoggerV1(path+'info.log')
    # log1.debug('一个debug信息')
    # log1.info('一个info信息')
    # log1.warn('一个warning信息')
    # log1.error('一个error信息')
    # log1.criti('一个致命critical信息')
    # print(log1.read_log())
    pass
