#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p14_t8_urrllib.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-26-下午11:00
# ---------------------说明--------------------------
# urllib提供了一系列用于操作URL的功能
# ---------------------------------------------------

def testUrlRequest3(url=None):
    """
    TODO 该urllib3的urlopen方法是抽象方法,目前还不知道如何调用urllib3的库以及和urllib的区别.
    :param url:
    :return:
    """
    from urllib3 import request
    httpbody = {}
    httpRequest = request.RequestMethods()
    httpResponse = httpRequest.request(method="GET", url=url)
    print(httpResponse)
    # with request.RequestMethods().urlopen(method='GET', url=url) as httpget:
    #     print("")
    #     httpget.read()


def testUrlRequest(geturl=None):
    from urllib import request
    # from urllib import response
    # import urllib
    # import httplib2

    with request.urlopen(geturl) as httpget:
        print(type(httpget))
        respHeader = httpget.getheaders()
        respData = httpget.read()
        print(type(respHeader), type(respHeader[0]), respHeader[0])
        for itemk, itemv in respHeader:
            print("httpResponseHeaders: [%s],[%s]" % (itemk, itemv))
        print("ResponseData:%s", respData.decode())
        # print(httpget.read())


def testPostRequest(posturl=None):
    from urllib import parse, request
    print('Login to weibo.cn...')
    email = input('Email: ')
    passwd = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])
    print(login_data)
    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


# Handler
#
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
def testProxyHandler():
    from urllib import request
    proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth_handler = request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        pass


testurl = "https://www.dytt8.net/"
testurl = "https://api.douban.com/v2/book/2129650"
# testUrlRequest(testurl)
testPostRequest(testurl)
# testUrlRequest3(testurl)
