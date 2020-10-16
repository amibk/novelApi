# novelApi

#### 介绍
小说书源模式的接口封装，支持搜索、查看小说详情、获取小说目录、获取章节内。
书源模式下本身不存储小说任何内容，所有数据皆来自源站，规避了版权风险

采用了轻量级的Flask作为web框架，开发环境为Python3.x，直接执行

```
python main.py
```
即可在本地浏览器中访问http://127.0.0.1:8088

直接体验可访问：https://novelapi.amibk.com/

## API接口列表
1. /search/{要搜索的小说关键字，支持模糊搜索}：搜索小说，如/search/天道图书馆
2. /page?url={小说连接}：获取小说信息和章节目录，url传递小说连接，必须对参数进行URL编码。如/page?url=http%3a%2f%2fwww.xbiquge.la%2f26%2f26001%2f
3. /content?link={章节连接}：获取小说的章节内容，link传递章节连接，必须对参数进行URL编码。如/content?link=%2f26%2f26001%2f12740369.html


## 用到的Python库有
1. flask
2. lxml
3. requests
4. fake_useragent

没有以上库的，需要先pip install 一下缺少的库


内置了一个小说站的规则，编写的通俗易懂，适合Python的采集新手、Flask新手、接口开发新手等进行参考

同时希望可以获得内容扩展和填充。



