#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: p5-3-range.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-11-下午10:47
# ---------------------说明--------------------------
# 列表生成式
# ---------------------------------------------------
userIdList = list(range(1, 10));
print(userIdList)
# 但是如何生成id经过特殊规则计算的迭代值呢？ 比如列表每个元素都是2的倍数。
userIdList2 = [item * 2 for item in range(1, 10)]
print(userIdList2)


# 可以，很强大了，但是能经过一个函数计算返回值吗
def _2nj1(x):
    return 2 * x + 1


userIdList3 = [_2nj1(item) for item in range(1, 10) if item % 2 == 0]
print(userIdList3)

# Question？ 用一行代码实现 ABC三个字母的所有排序组合
userIdList4 = [item + item2 for item2 in "ABC" for item in list("ABC")]
print(userIdList4)


def _jj():
    return range(1, 9)


userIdList5 = ["{0}*{1}={2}".format(item, item2, item * item2) for item2 in _jj() for item in _jj()]
print(userIdList5)

import os

homedir = [itemDir for itemDir in os.listdir()]
print(type(homedir), homedir)

# 列表生成式也可以用来使用两个变量来访问字典

d = {'x': 'A', 'y': 'B', 'z': 'C'}
dictREsu = [k + '=' + v for k, v in d.items()]
print(dictREsu)

# 把所有字符to小写

L = ['Hello', 'World', 'IBM', 'Apple',234]
lowchar = [s.lower() for s in L if isinstance(s, str)]
print(lowchar)
