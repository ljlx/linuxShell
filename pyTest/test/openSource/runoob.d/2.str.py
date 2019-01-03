#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: 2.str.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-3-下午6:24
# ---------------------说明--------------------------
# 字符串
# ---------------------------------------------------

# center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格参数
#
#     width -- 字符串的总宽度。
#     fillchar -- 填充字符
# 返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
# ----sss----
print("sss".center(11, '-'))

str = "[www.runoob.com]"

print("str.center(40, '*') :{} ", str.center(40, '*'))

testStr = ("abcd1234", "abcd", "1234", "##@@")

defDesc = {str.isalnum()}


def test(text: str, func):
    return func(text)


for item in testStr:
    result = test(item, str.isalnum)

print("字符串至少有一个字符并且所有字符都是字母或数字:{},结果:{}".format("abcd1234", "abcd1234".isalnum()))
print("字符串至少有一个字符并且所有字符都是字母或数字:{},结果:{}".format("abcd", "abcd".isalnum()))
print("字符串至少有一个字符并且所有字符都是字母或数字:{},结果:{}".format("1234", "1234".isalnum()))
print("字符串至少有一个字符并且所有字符都是字母或数字:{},结果:{}".format("###@@", "###@@".isalnum()))
print("字符串至少有一个字符并且所有字符都是字母:{},result:{}".format("123", "123".isalpha()))
print("字符串至少有一个字符并且所有字符都是字母:{},result:{}".format("123", "123".isalpha()))
