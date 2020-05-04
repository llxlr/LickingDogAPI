from settings import PIXIV_EMAIL, PIXIV_PASSWD
from pixivpy_async import *

main_url = "https://www.pixiv.net"
# client = PixivClient()
# aapi = AppPixivAPI(client=client.start())
# papi = PixivAPI(client=client)
# aapi.login(PIXIV_EMAIL, PIXIV_PASSWD)
# papi.login(PIXIV_EMAIL, PIXIV_PASSWD)


def connent():
    try:
        from settings import headers
        import requests
        r = requests.get(main_url, headers=headers)
        if r.status_code == 200:
            return True
    except Exception as e:
        del e
        return False


# class Pixiv:
#     def __init__(self, id=None, text=None):
#         self.id, self.text = id, text
#
#     def works(self):
#         return papi.works(self.id)
#
#     def search(self):
#         return papi.search_works(self.text, page=1, mode='text')


if __name__ == "__main__":
    print(connent())
    pass
