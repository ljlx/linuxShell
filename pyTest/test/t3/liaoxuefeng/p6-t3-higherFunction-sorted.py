#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: p6-t3-higherFunction-sorted.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-15-下午4:19
# ---------------------说明--------------------------
# 排序函数
# ---------------------------------------------------
import random

__author__ = 'hanxu'
__site__ = 'https://www.thesunboy.com'


def _2nj1(x):
    return 2 * x + 1


userIdList3 = [_2nj1(item) for item in range(1, 10) if item % 2 == 0]
print(userIdList3)


# 定义一个随机数,列表生成器,
def getRandom(numseed: int):
    jj = random.randint.__str__()
    print(jj)
    return jj


randomData = [getRandom(item) for item in range(1, 10)]
print(randomData)
for item in getRandom():
    print(next(item))
