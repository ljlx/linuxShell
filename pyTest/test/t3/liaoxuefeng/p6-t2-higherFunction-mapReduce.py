#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: p6-t2-mapReduce.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-13-下午11:12
# ---------------------说明--------------------------
# 大数据-流式计算 来自google发表的文章,影响到了java8和大数据stream平台
# http://research.google.com/archive/mapreduce.html
# --------------------------------------------------
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000
# python内建了map()和reduce()函数。
#
# 如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。
#
# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#
# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下


def f(x: int) -> int:
    """
    计算x的阶乘
    :param x:
    :return:
    """
    return x * x;


# 高阶函数map
xlists = list(range(1, 10));
print(xlists)
xlists2 = map(f, xlists)
xlists3 = list(xlists2)
# 和java一样 list相当于一个Terminal操作,stream将不可用了,不同的是java会抛出异常,而py不会
print(xlists3)
mapList = map(str, xlists3)
strlist = list(mapList)
print(mapList, strlist)

# 高阶函数reduce
from functools import reduce


def add3(x, y):
    return x + y


reduce(add3, [1, 3, 5, 7, 9])


#
# 但是如果要把序列[1, 3, 5, 7, 9]
# 变换成整数13579，reduce就可以派上用场：

def int2append(x, y):
    return str(x) + str(y)


def int2append2(x, y):
    return x * 10 + y


testdata = [1, 3, 5, 7, 9]
print(sum(testdata))
print(reduce(int2append, testdata))
print(reduce(int2append2, testdata))


# 实现一个str2int函数
def char2int(x: str) -> int:
    intmap = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return intmap[x]


def fn0(x, y):
    return x * 10 + y


def musum(x, y):
    return x + y


def str2int(x: str, fun=fn0) -> int:
    intmap = map(char2int, x)
    return reduce(fun, intmap)


# 测试数据,要求给出数字版的,和求和,且不能使用int()和sum()函数.
testdata1 = "1314520"

result1 = str2int(testdata1)
print(result1)
print(str2int(testdata1, musum))

# 整理成一个str2int的函数就是
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int2(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


# 还可以用lambda函数进一步简化成

def char2num2(s):
    return DIGITS[s]


def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num2, s))
