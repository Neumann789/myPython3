# -*- coding:utf8 -*-
# 使用WSGI作为服务器来处理浏览器请求
#  Created by fanghuabao on 2017/9/26.


from wsgiref.simple_server import make_server

def application(environ, start_response):

    # print("environ:", environ['PATH_INFO'])
    # 'Content-Type', 'text/html' 告诉浏览器什么样的数据
    start_response('200 OK', [('Content-Type', 'text/html')])

    path = environ['PATH_INFO']

    if path == '/book' or path == '/book/':

        return [b'<h1>Hello,book!</h1>']

    elif path == '/web' or path == '/web/':

        return [b'<h1>Hello,web!</h1>']

    else:

        return [b'<h1>404</h1>']



httpd = make_server('', 8005, application)

print('Serving HTTP on port 8000....')

httpd.serve_forever()
