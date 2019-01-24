#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p14_t4_struct.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-24-下午5:16
# ---------------------说明--------------------------
# stuct
# ---------------------------------------------------
"""
准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。

在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：
"""
n = 10240099
n1 = n & 0xff000000
n2 = n & 0xff0000
n3 = n & 0xff00
n4 = n & 0xff
b1 = n1 >> 24
b2 = n2 >> 16
b3 = n3 >> 8
b4 = n4
bs = bytes([b1, b2, b3, b4])
print(bs)
a = 12
b = 1
c = 0


def ss():
    print("a的16进制值:", int(b'abc'.hex(), base=16))
    # result:97
    # 该值相当于java代码"a".getBytes()[0] == 97


ss()
