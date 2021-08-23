#!/usr/bin/env python
# -*- coding: utf-8 -*-
from amzqr import amzqr
import time
import os
"""
words：二维码内容，链接或者句子
version：二维码大小，范围为[1, 40]
level：二维码纠错级别，范围为{L, M, Q, H}，H为最高级，默认。
picture：自定义二维码背景图，支持格式为.jpg，.png，.bmp，.gif，默认为黑白色
colorized：二维码背景颜色，默认为False，即黑白色
contrast：对比度，值越高对比度越高，默认为1.0
brightness：亮度，值越高亮度越高，默认为1.0，值常和对比度相同
save_name：二维码名称，默认为qrcode.png
save_dir：二维码路径，默认为程序工作路径
"""
timestamp = time.time()
version, level, qr_name = amzqr.run(
    words='hello world!',
    save_name=f'{timestamp}-temp.png',
    save_dir='../cache/',
)
print(version, level, qr_name)
os.remove(f'../cache/{timestamp}-temp.png')
