#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p15_t3_chardet.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx9409i29/linuxShell
# Created Time: 2019-1-28-下午8:24
# ---------------------说明--------------------------
# 字符串编码第三方库 chardet,默认在anaconda计算平台已经安装好了.
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001510905171877ca6fdf08614e446e835ea5d9bce75cf5000#0
# ---------------------------------------------------
# 字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。虽然Python提供了Unicode表示的str和bytes两种数据类型，并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes做decode()不好做。
#
# 对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。
#
# 当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。

def getStrByte(testStr: str = None, encodeType: str = 'utf8') -> bytes:
    """
    将字符串按照指定的编码类型返回
    :param encodeType:  编码类型,utf8,gb2312,gbk
    :return: 字符的编码字节对象.
    """

    print("测试字符串:", testStr)
    print("测试编码类型:", encodeType)
    testStrbype = testStr.encode(encodeType)
    print("编码的字节:", testStrbype)
    return testStrbype


def detectionBytes(textBytes: bytes):
    import chardet
    detextResult = chardet.detect(textBytes)
    print(detextResult)


if __name__ == '__main__':
    detectionBytes(getStrByte("hello.world", 'utf8'))
    detectionBytes(getStrByte("韩旭，一岁一枯荣", 'gbk'))
    detectionBytes(getStrByte("韩旭，一", 'gbk'))
    detectionBytes(getStrByte("韩旭", 'gb2312'))
    detectionBytes(getStrByte("韩旭", 'utf8'))
    detectionBytes(getStrByte('离离原上草，一岁一枯荣', 'gbk'))
    detectionBytes(getStrByte('离离原上草，一岁一枯荣', 'utf8'))
    detectionBytes(getStrByte('最新の主要ニュース', 'euc-jp'))
    detectionBytes(getStrByte('最新の主要ニュース', 'utf-8'))
    detectionBytes(getStrByte('我爱你', 'utf-8'))
    detectionBytes(getStrByte('我爱你', 'gbk'))
    detectionBytes(getStrByte('我爱你', 'gb2312'))
    detectionBytes(getStrByte('天王盖地虎', 'utf-8'))
    detectionBytes(getStrByte('天王盖地虎', 'gbk'))
    detectionBytes(getStrByte('天王盖地虎', 'gb2312'))
    # 经试验，和字数有关系，字数越多越容易识别出来
    detectionBytes(getStrByte('天王盖地哈哈哈哈哈就是就是', 'utf-8'))
    detectionBytes(getStrByte('天王盖地哈哈哈哈哈就是就是', 'gbk'))
    detectionBytes(getStrByte('天王盖地哈哈哈哈哈就是就是', 'gb2312'))
    detectionBytes(getStrByte('天王盖地虎,小鸡炖蘑菇', 'utf-8'))
    detectionBytes(getStrByte('天王盖地虎,小鸡炖蘑菇', 'gbk'))
    detectionBytes(getStrByte('天王盖地虎,小鸡炖蘑菇', 'gb2312'))

#     检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。
# 检测的编码是GB2312，注意到GBK是GB2312的超集，两者是同一种编码，检测正确的概率是74%，language字段指出的语言是'Chinese'。

# 可见，用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理。
#
# chardet支持检测的编码列表请参考官方文档Supported encodings。
# https://chardet.readthedocs.io/en/latest/supported-encodings.html
