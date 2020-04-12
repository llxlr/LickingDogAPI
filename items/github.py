from settings import headers
from lxml import etree
import requests
import re

cdn = 'https://cdn.jsdelivr.net/gh/jamesyangget/LickingDogAPI/data/'
languages = requests.get(cdn+'language.json', headers=headers).json()
spoken_langs = requests.get(cdn+'spoken_language.json', headers=headers).json()
list_xp = '//article[@class="Box-row"]'
trend_xp = [
    '//h1[@class="h3 lh-condensed"]/a/@href',
    '//p/text()',
    '//span[@itemprop="programmingLanguage"]/text()',
    '//a[@class=" muted-link d-inline-block mr-3"]/text()'
]
dev_xp = [
    '',
    '',
    '',
    '',
    '',
]


def url(type_, spoken_lang, language, date):
    trending = 'https://github.com/trending'
    developers = trending + '/developers'
    url_ = ''
    if type_ == 'trending':
        url_ = trending
        if list(filter(lambda x: x["language"] == language, languages)):
            if list(filter(lambda x: x["spoken_language"] == spoken_lang, spoken_langs)):
                if date in ['daily', 'weekly', 'monthly']:
                    url_ += '/{}?since={}&spoken_language_code={}'.format(language, date, spoken_lang)
            else:
                if date in ['daily', 'weekly', 'monthly']:
                    url_ += '/?since={}&spoken_language_code={}'.format(date, spoken_lang)
        else:
            if date in ['daily', 'weekly', 'monthly']:
                url_ += '/?since={}'.format(date)
    elif type_ == 'developers':
        url_ = developers
        if list(filter(lambda x: x["language"] == language, languages)):
            if date in ['daily', 'weekly', 'monthly']:
                url_ += '/{}?since={}'.format(language, date)
        else:
            if date in ['daily', 'weekly', 'monthly']:
                url_ += '/?since={}'.format(date)
    return url_


class Github(object):
    def __init__(self, type_, spoken_lang, language, date):
        self.type, self.spoken_lang, self.language, self.date = type_, spoken_lang, language, date

    @staticmethod
    def dom_parse(html, xpath):
        dom_tree = etree.HTML(html)
        return dom_tree.xpath(xpath)

    def trending(self):
        url_, data = url(self.type, self.spoken_lang, self.language, self.date), []
        html = self.dom_parse(requests.get(url_, headers=headers).text, list_xp)
        block = map(lambda x: etree.tostring(x), html)
        # print(list(data))
        for y in block:
            y = bytes.decode(y)

            # t = self.dom_parse(y, trend_xp[0])
            # user, repo = t[0][1:].split('/')
            # data.append(repo)

            # t = self.dom_parse(y, trend_xp[1])
            # if t:
            #     data.append(t[0].strip())
            # else:
            #     data.append('')

            # t = self.dom_parse(y, trend_xp[2])
            # if t:
            #     lang = t[0]
            #     data.append(lang)
            # else:
            #     data.append('')

            t = self.dom_parse(y, trend_xp[3])
            if len(t) == 4:
                data.append((t[1].strip(), t[3].strip()))
            elif len(t) == 2:
                data.append(t[1].strip())
            else:
                data.append('')
        # {"username": user, "repo": repo, "description": description, "language": lang, "star": star, "fork": fork}
        return data

    def developers(self):
        url_, data = url(self.type, self.spoken_lang, self.language, self.date), []
        html = etree.HTML(requests.get(url_, headers=headers).text)
        # {"rank": rank,"avatar": avatar,"nickname": nick,"username": user,"repo": repo,"description": description}
        return data


if __name__ == '__main__':
    # print(url("trending", None, None, "daily"))
    print(Github("trending", None, None, "daily").trending())
    # t = etree.HTML(b'<p class="col-9 text-gray my-1 pr-4">\\n      Azure Quickstart Templates\\n    </p>\\n\\n  ')
    # print(list(map(lambda x: x.replace('\\n', '').strip(), t.xpath('//p/text()'))))
    pass
