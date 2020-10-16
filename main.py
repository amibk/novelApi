from flask import Flask
from Api import biquge
import logging
from flask import request

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
bqg = biquge()


@app.route('/')
def index():
    str = """
    接口列表：
    <br/> 
    1、/search/{要搜索的小说关键字，支持模糊搜索}：搜索小说，如/search/天道图书馆<br/> 
    2、/page?url={小说连接}：获取小说信息和章节目录，url传递小说连接，必须对参数进行URL编码。如/page?url=http%3a%2f%2fwww.xbiquge.la%2f26%2f26001%2f<br/> 
    3、/content?link={章节连接}：获取小说的章节内容，link传递章节连接，必须对参数进行URL编码。如/content?link=%2f26%2f26001%2f12740369.html
    
    """
    return str, 200, {'Content-Type': 'text/html; charset=utf-8'}


@app.route('/search/<name>')
def search(name):
    searchResult = bqg.search(name)
    return searchResult, 200, {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/page', methods=['GET'])
def page():
    url = request.args.get('url')
    if url is None:
        return '主要参数[url]不存在', 200
    pageResult = bqg.page(url)
    return pageResult, 200, {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/content', methods=['GET'])
def content():
    url = request.args.get('link')
    if url is None:
        return '主要参数[link]不存在', 200
    contentResult = bqg.content(url)
    return contentResult, 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__ == '__main__':
    app.run(port=8088, debug=False)
