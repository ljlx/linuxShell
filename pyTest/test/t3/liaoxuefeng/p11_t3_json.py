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
# https://www.jb51.net/article/139498.htm 关于json库的详细说明
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138683221577998e407bb309542d9b6a68d9276bc3dbe000
# JSON
#
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
#
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
# 参考/usr/lib/python3.5/json/encoder.py
# +-------------------+---------------+
# | Python            | JSON          |
# +===================+===============+
# | dict              | object        |
# +-------------------+---------------+
# | list, tuple       | array         |
# +-------------------+---------------+
# | str               | string        |
# +-------------------+---------------+
# | int, float        | number        |
# +-------------------+---------------+
# | True              | true          |
# +-------------------+---------------+
# | False             | false         |
# +-------------------+---------------+
# | None              | null          |
# +-------------------+---------------+

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
print("py对象->json字符串:", jsonStr)

jsonobj = json.loads(jsonStr)
print("json字符串->py对象:{}".format(jsonobj))


# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


# json.dumps(s)


# TypeError: <__main__.Student object at 0x7f38856d9f60> is not JSON serializable

def stu2json(stu: Student):
    return {"name": stu.name, "age": stu.age, "score": stu.score}
    # return testjson

    stu2json2 = lambda stu: stu.__dict__
    # 自定义序列化,使用default参数来格式化类对象
    stujsonstr = json.dumps(s, default=stu2json2)
    print(stujsonstr)


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


# 自定义类,反序列化,使用object_hook来设置函数
json_str = '{"age": 20,  "name": "小红","score":120}'
stu2 = json.loads(json_str, object_hook=dict2student, encoding='utf-8')


def testjson2dict(obj):
    print(obj)
    return obj


print("准备实验复杂多层次json,使用objHook解析json,分别构造对象的过程: {}".format(jsonStr))
stu2 = json.loads(jsonStr, object_hook=testjson2dict, encoding='utf-8')

# json.dump()

print(stu2)
# 3.6
# 非字符串类型键名

# 在Python中, 只是可哈希(hashable)的对象和数据都可以做为Dictionary对象的键, 而JSON规范中则只能使用字符串做为键名.
# 所以在json.dumps的实现中, 对这个规则进行了检查, 不过键名允许的范围有所扩大, str, int, float, bool和None类型的数据都可以做为键名.
# 不过当键名非str的情况时, 键名会转换为对应的str值
# json.dumps的skipkeys参数可以改变这个行为. 当将skipkeys设置为True时, 遇到非法的键名类型, 不会抛出异常, 而是跳过这个键名:
# strFile = "/tmp/p11-t3-json/jsonstore.json"
strFile = "/home/hanxu/document/project/code/personal/develop/linuxShell/pyTest/test/utils-py/debug.json"
fileJson = open(file=strFile, mode="r")
# strline = fileJson.readline(1)
debugjsonFileContent = ""
if fileJson.readable():
    debugjsonFileContent = fileJson.read()
debugjsonObj = json.loads(debugjsonFileContent)
print(debugjsonObj)
fileJson.close()
# print(strline);

