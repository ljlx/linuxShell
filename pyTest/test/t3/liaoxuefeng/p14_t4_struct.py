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
# TODO 该类用于方便字节类操作,以后需要的时候深度学习.
# ---------------------------------------------------
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431955007656a66f831e208e4c189b8a9e9f3f25ba53000
"""
准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。

在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：
"""


def int2byte(num: int):
    n = num
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


int2byte(10240099)
int2byte(96)
int2byte(6382179)
int2byte(448311228533)


def ss():
    print("abc的16进制值:", int(b'hanxu'.hex(), base=16))
    abcBa = bytearray()
    for item in 'abc':
        itemb = item.encode()
        itemint = int(itemb.hex(), base=16)
        print(itemint)
        abcBa.append(itemint)
    print(abcBa)
    # result:97
    # 该值相当于java代码"a".getBytes()[0] == 97


ss()


# 非常麻烦。如果换成浮点数就无能为力了。
#
# 好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
#
# struct的pack函数把任意数据类型变成bytes

def testStruct_pack():
    import struct
    # pack的第一个参数是处理指令，'>I'的意思是：
    #
    # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
    #
    # 后面的参数个数要和处理指令一致
    t1 = struct.pack('>I', 10240099)
    print(t1)

def testWindowBmp():
    s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
    print(s)

