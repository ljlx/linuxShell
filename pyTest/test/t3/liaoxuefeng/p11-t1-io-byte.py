#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p11-t1-io-byte.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-7-下午3:37
# ---------------------说明--------------------------
# byte的操作和学习
# ---------------------------------------------------

# 一.byte的定义
# 1.使用bytes()定义

def creBytes():
    """
    使用bytes函数创建bytes
    :return:
    """
    emptyByte = bytes()
    init0Byte = bytes(10)
    int12bytes = bytes([12, 12, 12])
    print("空字节类型:", emptyByte)
    print("init0Byte", init0Byte)
    print("int12bytes", int12bytes)

    # 2.直接定义


def testByte():
    b = (b'python')
    barr = (b'p'b'y'b't')
    print(b)
    print(barr)
    print(b[0])
    # 我们可以用 b"*" 的形式创建一个字节类型，前提条件是这里的 * 必须是 ASCII 中可用的字符，否则将会超出限制
    # 那么问题来了，我们发现上面的 ASCII 表里面所有的字符只占据了 [31, 127]，那对于这一范围之外的数字我们要怎么才能表示为字节类型？答案就是用特殊的转义符号x+十六进制数字
    # [31,127] 之外的应该是一些控制字符,无法直接显示的
    # 0～31及127(共33个)是控制字符或通信专用字符（其余为可显示字符
    # 32～126(共95个)是字符(32是空格）,其中48～57为0到9十个阿拉伯数字。
    # 65～90为26个大写英文字母，97～122号为26个小写英文字母，其余为一些标点符号、运算符号等
    # https://baike.baidu.com/item/ASCII/309296?fr=aladdin
    print("字节对象:", b'xjjj', type(b'xjjj'))
    print("字节对象decode:", b'xjjj'.decode(), type(b'xjjj'.decode()))
    print(b'x24')
    print(b'xjjj'.__len__())
    byteData = bytes([66, 67, 68])
    print("字节转字符:", byteData)
    print("字节转16进制:", byteData.hex())
    print("从16进制转成字节对象,在以ascii打印", bytes.fromhex("6e 7a 7b 7c 7d 42"))
    print("从字符B转成字节,在转成16进制:", b'B'.hex())
    print("测试int的构造参数,int类型:", int(123456))
    print("测试int的构造参数,字符串类型:", int("123456"))

    print("测试int的构造参数,将字母B,转成16进制字符串,再以16进制解析该字符串为10进制的数字:", int(b'B'.hex(), base=10))
    print("测试int的构造参数,以10进制解析字符串[42]为10进制的数字:", int("42", base=10))
    print("测试int的构造参数,以16进制解析字符串[42]为10进制的数字:", int("42", base=16))
    allascii = []
    for i in range(32, 126):
        bytesi = bytes([i])
        # print("字节位[{}],转译字符[{}],Hex[{}]".format(i, bytesi, bytesi.hex()))
        allascii.append(str(bytesi))
        # print(allascii)


# 二.类型转换

# string.encode()
# int.tobytes()
# bytes.from

# 三.bytes的显示方式
# 只有ASCII中的字符串是可以直接在bytes类型中显示出来的，所有大于127的数值用转义字符表达(也就是b'\xe5\x90\',这样类似,使用x来表示的)。
# 只有ASCII中的字符串是可以直接在bytes类型中显示出来的，所有大于127的数值用转义字符表达。
#
# 比如，内存中的字节对象用十六进制表示为61，在python中显示的方式不是b'\x61' 而是b'a'；而b'\xe4'显示方式就是b'\xe4'；注意：仅仅是显示方式而已
#
# 另外，并不是所有的小于127的都可以被友好的显示出来，有些对象本身不可显示，就显示其十六进制表示。比如

# bytes的一般方法.
def testBytesMethod():
    bhx = b'\x68\x78'
    bspace = b'\x2B'
    btemp = b'\x74\x74'  # 占位符
    btempindex = b'hanxttu'.find(btemp)
    bhanxu = b'hanxttu'.replace(btemp, bspace)

    print(bhanxu)
    print(bhanxu.decode())


# bytearray定义
# https://www.cnblogs.com/dingtianwei/p/9459575.html
# bytearray是可变的bytes数据类型,可以通过bytearray创建和定义.
# 一：bytearray()定义
#
# bytearray() 创建一个空的bytearray
# bytearray(int) 创建一个int位的全位0的bytearray
# bytearray(iterabl_of_ints) 可迭代数字组成的bytearray(比如range)
# bytearray(string,encoding[,errors]) 将一个字符串编码为bytearray
# bytearray(bytes of buffer) 创建一个bytearray
#
# 二: bytearray的方法定义
#
# bytearray.fromhex()

def initByteArrays():
    ba = bytearray()
    print("创建空的字节数组:", ba,ba.decode())
    ba10 = bytearray(10)
    print("创建10个长度,全为0的bytearray", ba10,ba10.decode())
    barange10 = bytearray(range(1, 10))
    # int.from_bytes(barange10,byteorder=)
    print("可迭代数字bytesarray:", barange10,barange10.decode())
    bachar = bytearray("hello爱.bytearrays", encoding='utf-8')
    print("字符转bytearray:", bachar,bachar.decode())


if __name__ == '__main__':
    # testByte()
    # creBytes()
    # testBytesMethod()
    initByteArrays()
