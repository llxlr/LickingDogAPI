#!/usr/bin/env python
# -*- coding: utf-8 -*-
import twint


class TW:
    def __init__(self, uid, username=None,
                 proxy_host=None,
                 proxy_port=None,
                 proxy_type=None):
        self.c = twint.Config()
        self.username = username if username else None
        self.uid = uid
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_type = proxy_type

    def setup_proxy(self):
        self.c.Proxy_host = self.proxy_port
        self.c.Proxy_port = self.proxy_port
        self.c.Proxy_type = self.proxy_type

    def save_data(self):
        pass
