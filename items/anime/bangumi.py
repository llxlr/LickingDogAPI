from settings import headers
import requests
import time


class Bangumi(object):
    """"""
    def __init__(self, id):
        super(Bangumi, self).__init__()
        self.id = id
