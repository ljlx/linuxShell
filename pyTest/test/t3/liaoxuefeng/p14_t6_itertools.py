#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p14_t6_itertools.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-25-下午9:20
# ---------------------说明--------------------------
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
# ---------------------------------------------------
import itertools

test = True


def printClassInfo(obj: object):
    if obj:
        objclass = obj.__class__
        print(objclass.mro())


def testNatualsCount(isxiaofei=True, step=100):
    natuals = itertools.count(start=1, step=step)
    printClassInfo(natuals)
    if not test:
        return
    if isxiaofei:
        for item in natuals:
            print(item)
    else:
        return natuals


def testRecyke():
    natuals = itertools.cycle("abcdefg")
    printClassInfo(natuals)
    if not test:
        return
    for item in natuals:
        print(item)


def testReoeat():
    natuals = itertools.repeat('a', times=3)
    printClassInfo(natuals)
    if not test:
        return
    for item in natuals:
        print(item)


# TODO 无限序列 应该是之前介绍过得高阶函数.实现的.
# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
#
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列

def funcTakeWhile(x: int):
    if isinstance(x, int):
        return x <= 10
    if isinstance(x, str):
        return True


def testTakeWhile(natuals=None):
    # takewhileNatuals = itertools.takewhile(lambda x: x <= 10, natuals)
    if not natuals:
        natuals = itertools.repeat('abc', times=3)
    takewhileNatuals = itertools.takewhile(funcTakeWhile, natuals)
    printClassInfo(takewhileNatuals)
    if not test:
        return
    takewhileNatualsList = list(takewhileNatuals)
    for item in takewhileNatualsList:
        print(item)


def testChain(isreturn: bool = False):
    """
    chain 可以把一组迭代对象串联起来,形成一个更大的迭代器.
    :return:
    """
    t1 = itertools.repeat('abc', times=3)
    t2 = itertools.repeat('def', times=3)
    t3 = itertools.cycle("abcd")
    tchain = itertools.chain(t1, t2, t3)
    if isreturn:
        return tchain
    for item in tchain:
        print(item)


def testGroups():
    """
    groupby()把迭代器中相邻的重复元素挑出来放在一起
    ,实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
    这两个元素就被认为是在一组的，而函数返回值作为组的key。
    如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
    :return:
    """
    tchain = testChain(True)

    def filerKey(key: str):
        print("key:", key)
        return key.lower()

    tgroup = itertools.groupby('AaaBBbcCAAa', key=filerKey)
    for key, group in tgroup:
        print("key:[%s], valueList:[%s]" % (key, list(group)))


# 作业:
# def pi(N):
#     ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
#
#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
#
#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
#
#     # step 4: 求和:
#     return 3.14

def pi(N: int = 10):
    import itertools, functools, math
    # 从1开始,步进为2,进行取一个声明列表
    oddNumList = itertools.count(start=1, step=2)

    filter = lambda x: x <= 2 * N - 1
    oddNumListLimit = list(itertools.takewhile(filter, oddNumList))

    print("计算该list:", oddNumListLimit)

    # def sss(x):
    #     # x**y
    #     oddnum = oddNumListLimit.index(x)
    #     # 计算是否需要取负数
    #     powValue = math.pow(-1, oddnum)
    #     return powValue * 4 / x
    mapFun = lambda x: math.pow(-1, oddNumListLimit.index(x)) * 4 / x
    # 将列表的每个元素进行函数计算后,返回替换原来的值
    convertValueList = map(mapFun, oddNumListLimit)
    result = functools.reduce(lambda x, y: x + y, convertValueList)
    print(result)


def pi2(N):
    import itertools, math
    from functools import reduce
    odds = itertools.count(1, 2)
    ns = list(itertools.takewhile(lambda x: x <= 2 * N - 1, odds))
    pp = reduce(lambda x, y: x + y, map(lambda x: math.pow(-1, ns.index(x)) * 4 / x, ns))
    print(pp)

if __name__ == '__main__':
    # testNatualsCount()
    # testRecyke()
    # testReoeat()
    # natuals = testNatualsCount(True, 2)
    # testTakeWhile(natuals)
    # testChain()
    # testGroups()
    # pi()
    pi2(10)
    pi2(100)
    pi2(1000)
    pi2(10000)
    pi2(100000)
    # TODO 利用分布式计算的功能来快速计算出结果.
