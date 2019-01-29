#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p15_t3_chardet.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-28-下午8:24
# ---------------------说明--------------------------
# 字符串编码第三方库 chardet,默认在anaconda计算平台已经安装好了.
# ---------------------------------------------------
# 字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。虽然Python提供了Unicode表示的str和bytes两种数据类型，并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes做decode()不好做。
#
# 对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。
#
# 当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。

def getStrByte(encodeType: str) -> bytes:
    """
    将字符串按照指定的编码类型返回
    :param encodeType:  编码类型,utf8,gb2312,gbk
    :return: 字符的编码字节对象.
    """
    testStr = "hello.world旭666"
    print("测试字符串:", testStr)
    print("测试编码类型:", encodeType)
    testStrbype = testStr.encode(encodeType)
    return testStrbype


if __name__ == '__main__':
    testbytes = getStrByte('utf8')
    print(testbytes)
