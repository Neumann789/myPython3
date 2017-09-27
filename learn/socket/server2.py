# -*- coding:utf8 -*-
# TODO 功能描述
#  Created by fanghuabao on 2017/9/26.

from wsgiref.simple_server import make_server

def application(environ, start_response):

    # 'Content-Type', 'text/html' 告诉浏览器什么样的数据
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello,web!</h1>']


def application2(environ, start_response):

    # 'Content-Type', 'text/html' 告诉浏览器什么样的数据
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello,web!</h1>']

httpd = make_server('', 8000, application)

print('Serving HTTP on port 8000....')

httpd.serve_forever()
