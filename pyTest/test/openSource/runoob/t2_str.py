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
# http://www.runoob.com/python3/python3-string.html
# center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格参数
#
#     width -- 字符串的总宽度。
#     fillchar -- 填充字符
# 返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
# ----sss----
print("sss".center(11, '-'))

str = " [www.runoob.com] "
# strip和java的trim一样.不过py有lstrip->left strip,和rstrip->right strip
str = str.strip()
print("str.center(40, '*') :{} ", str.center(40, '*'))

testStrTuple = ("abcd1234", "abcd", "1234", "##@@", "  ", " a ", "Abc", "ABC", "abc", "Abc123", "ABC123")


def test(text: str, func):
    # 这两个写法都是错的.
    # result = text.func()
    # func(text) 也是错的
    funcname = func.__name__
    funcc = getattr(text, funcname)
    result = funcc()
    #  使用反射方式来批量测试字符串方法调用
    return result


# 查看当前定义的全局变量
# allField = globals()
# 查看当前引入的模块
# xdir = dir()
# print("allfield:%s" % allField)
# print("dir():%s" % xdir)

for item in testStrTuple:
    print("当前测试字符串:{}".format(item))
    print("字符串至少有一个字符并且所有字符都是字母或数字:{},结果:{}".format(item, test(item, str.isalnum)))
    print("字符串至少有一个字符并且所有字符都是字母:{},result:{}".format(item, test(item, str.isalpha)))
    print("字符串只包含数字:{},result:{}".format(item, test(item, str.isdigit)))
    print("字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写:{},result:{}".format(item, test(item, str.islower)))
    print("字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写:{},result:{}".format(item, test(item, str.isupper)))
    print("字符串中只包含数字字符:{},result:{}".format(item, test(item, str.isnumeric)))
    print("字符串中只包含空白:{},result:{}".format(item, test(item, str.isspace)))
    print("字符串是标题化的,见title():{},result:{}".format(item, test(item, str.istitle)))
    print("返回字符串长度:{},result:{}".format(item, test(item, str.__len__)))
    # strip 剥夺；剥去
    print("截掉字符串左边的空格或指定字符:{},result:{}".format(item, test(item, str.lstrip)))

    print("\n")

# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# maketrans()
# TODO 学习记录.
