#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p11-t3-json.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-3-上午11:00
# ---------------------说明--------------------------
# json到对象的转换操作
# ---------------------------------------------------
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138683221577998e407bb309542d9b6a68d9276bc3dbe000
# JSON
#
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
#
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
# JSON类型 	Python类型
# {} 	dict
# [] 	list
# "string" 	'str'或u'unicode'
# 1234.56 	int或float
# true/false 	True/False
# null 	None

import json
from datetime import datetime as xdate

today = test3 = xdate.today()
print(today)
dict1 = dict(test1=111, test2="asdf")
list1 = list()
list1.append(dict1)
list1.append(dict(test1=2, test2="testt22"))
list1.append(dict(test1=3, test2="testt33"))
list1.append(dict(test1=3, test2=True))
list1.append(dict(test1=3, test2=today.strftime("%Y-%m-%d %H:%M:%S")))

testjson = dict(jarray=list1, test="jsontest")
testjson = dict(subjson=testjson, title="jsonTitle")
jsonStr = json.dumps(testjson)
print("py对象->json字符串:" + jsonStr)

jsonobj = json.loads(jsonStr)
print("json字符串->py对象:{}".format(jsonobj))
