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
    # 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
    t2 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
    print(t2)


def testWindowBmp():
    s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
    print(s)
    # BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
    #
    # 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
    # 一个4字节整数：表示位图大小；
    # 一个4字节整数：保留位，始终为0；
    # 一个4字节整数：实际图像的偏移量；
    # 一个4字节整数：Header的字节数；
    # 一个4字节整数：图像宽度；
    # 一个4字节整数：图像高度；
    # 一个2字节整数：始终为1；
    # 一个2字节整数：颜色数。
    import struct
    #     所以说用struct来按字节数量来解析字符,unpack方法要简单许多
    bmpbyteObj = struct.unpack('<ccIIIIIIHH', s)
    print("使用unpack解析出的类型为:%s,内容是:%s" % (type(bmpbyteObj), bmpbyteObj))
    # 结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。
    # TODO 改天尝试自己实现: 我想应该可以使用类似的方法来解析tcp包的数据,和http头的数据

testWindowBmp()
