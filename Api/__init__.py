# -*- coding: UTF-8 -*-

from lxml import etree
import requests
from fake_useragent import UserAgent
import json

ua = UserAgent()


def post(url, params):
    header = {
        'User-Agent': ua.random
    }
    res = requests.post(url=url, data=params, headers=header)
    res.encoding = 'utf-8'
    return res.text


def get(url):
    header = {
        'User-Agent': ua.random
    }
    res = requests.get(url=url, headers=header)
    res.encoding = 'utf-8'
    return res.text


class biquge:
    def __init__(self):
        self.searchUrl = "http://www.xbiquge.la/modules/article/waps.php"
        self.baseUrl = "http://www.xbiquge.la"

    def search(self, key):
        page = post(self.searchUrl, {'searchkey': key})
        searchHtml = etree.HTML(page)
        searchList = searchHtml.xpath('//*[@id="checkform"]/table/tr')
        resList = []
        for i in searchList:
            name = i.xpath('td[1]/a/text()')
            if len(name) == 0:
                continue
            else:
                name = name[0]
            link = i.xpath('td[1]/a/@href')[0]
            author = i.xpath('td[3]/text()')[0]
            lastTime = i.xpath('td[4]/text()')[0].strip()
            item = {'name': name, 'link': link, 'author': author, 'lastTime': lastTime}
            resList.append(item)
        return json.dumps(resList, ensure_ascii=False)

    def page(self, pageUrl):
        html = get(pageUrl)
        _data = etree.HTML(html)
        _list = _data.xpath('//*[@id="list"]/dl/dd')
        item = {'img': _data.xpath('//*[@id="fmimg"]/img/@src')[0],
                'desc': _data.xpath('//*[@id="intro"]/p[2]/text()')[0]}
        _listArray = []
        for n in _list:
            name = n.xpath('a/text()')[0]
            link = n.xpath('a/@href')[0]
            _listArray.append({'name': name, 'link': link})
        item['list'] = _listArray
        return json.dumps(item, ensure_ascii=False)

    def content(self, contentUrl):
        html = get(self.baseUrl + contentUrl)
        _data = etree.HTML(html)
        contentStr = _data.xpath('//*[@id="content"]/text()')
        textTmp = ''
        for s in contentStr:
            b = s.replace(u'\xa0', u'')
            textTmp = textTmp + "\n" + b
        item = {'str': textTmp}
        return json.dumps(item, ensure_ascii=False)