#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ipv4是32位地址，分成4段，每段之间都有"."分开，而每段之间有8位，范围0-255，示例：192.168.1.1；
ipv6是128位地址，每个数目等于4位（0-F）16位进制，4个一组，每段之间由“：”隔开，共有8段，其中如
果有连续性的"0"，如FE80:0000:0000:0000:0000:0000:0000:DE4F可以省略，写成FE80::DE4F，示
例：FE80:98FA::B45A
"""
import requests


def ip():
    return requests.get('https://api.ip.sb/ip').text
