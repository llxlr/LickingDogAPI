from settings import headers
from lxml import etree
import requests

cdn = 'https://cdn.jsdelivr.net/gh/jamesyangget/LickingDogAPI/data/'
languages = requests.get(cdn+'language.json', headers=headers).json()
spoken_langs = requests.get(cdn+'spoken_language.json', headers=headers).json()


def full_url(*args):
    type_, spoken_lang, language, date = args
    trending = 'https://github.com/trending'
    developers = trending + '/developers'
    url = ''
    if type_ == 'trending':
        if list(filter(lambda x: x["language"] == language, languages)):
            if list(filter(lambda x: x["spoken_language"] == spoken_lang, spoken_langs)):
                if date in ['daily', 'weekly', 'monthly']:
                    url = trending + '/{}?since={}&spoken_language_code={}'.format(language, date, spoken_lang)
            else:
                if date in ['daily', 'weekly', 'monthly']:
                    url = trending + '/{}?since={}&spoken_language_code={}'.format(language, date, spoken_lang)
    elif type_ == 'developers':
        if list(filter(lambda x: x["language"] == language, languages)):
            if date in ['daily', 'weekly', 'monthly']:
                url = developers + '/{}?since={}'.format(language, date)
        else:
            if date in ['daily', 'weekly', 'monthly']:
                url = developers + '/{}?since={}'.format(language, date)
    return url


def dom_parse(html, xpath):
    dom_tree = etree.HTML(html)
    return dom_tree.xpath(xpath)


class Github(object):
    def __init__(self, type_, options):
        self.type = type_
        self.options = options

    def trending(self):
        url, data = full_url(self.options), []
        html = requests.get(url, headers=headers).content.decode('utf-8')
        # {"username": username, "repo": repo, "description": description, "language": lang, "star": star, "fork": fork}
        return data

    def developers(self):
        url, data = full_url(self.options), []
        html = requests.get(url, headers=headers).content.decode('utf-8')
        # {"rank": rank,"avatar": avatar,"nickname": nickname,"username": username,"repo": repo,"description": description}
        return data


if __name__ == '__main__':
    lang = 'python'
    if list(filter(lambda x: x["language"] == lang, languages)):
        print(True)
    # print(list())
    pass
