from settings import headers
from random import randint
import requests


def hitokoto():
    cdn = 'https://cdn.jsdelivr.net/gh/jamesyangget/LickingDogAPI/data/'
    data = requests.get(cdn + 'hitokoto.json', headers=headers).json()
    return data[randint(1, len(data))]
