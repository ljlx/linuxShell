#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p9-t3-enum.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2018-11-11-上午9:54
# ---------------------说明--------------------------
# 枚举使用
# ---------------------------------------------------

# ----------start----------常量方式定义枚举元素----------start----------

RED = 1
BLUE = 2

# ----------end------------常量方式定义枚举元素----------end------------


# ----------start----------使用预制枚举类型----------start----------
# from enum import *
from enum import Enum, unique

allcolor = Enum('allcolor', ('red', 'blue', 'blank'))
print(allcolor)
for item in allcolor:
    print(item)


# ----------end------------使用预制枚举类型----------end------------


# ----------start----------自定义枚举类----------start----------
# @unique装饰器可以帮助我们检查保证没有重复值

@unique
class myenum(Enum):
    enum1 = 1
    enum2 = 2
    enum3 = 3


var1 = myenum.enum1
var2 = myenum.enum2
print(var1)
print(var2)
print(var1.name)
print(var2.value)
print(var1 == myenum.enum1)
print(myenum['enum1'])
print(myenum.enum1)
print(myenum(2))


for name,member in myenum.__members__.items():
    print('name:{},item:{}'.format(name,member))
# ----------end------------自定义枚举类----------end------------
