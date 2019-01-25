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


def testNatualsCount():
    natuals = itertools.count(start=1, step=1000)
    for item in natuals:
        print(item)


def testRecyke():
    natuals = itertools.cycle("abcdefg")
    for item in natuals:
        print(item)


def testReoeat():
    natuals = itertools.repeat('a', times=3)
    for item in natuals:
        print(item)


if __name__ == '__main__':
    # testNatualsCount()
    # testRecyke()
    testReoeat()
