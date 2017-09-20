'''
Created on 2017年9月20日

@author: fanghuabao
'''
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.baidu.com")

print(html)