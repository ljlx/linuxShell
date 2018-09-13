#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: p5-t5-Iterable.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-13-下午1:10
# ---------------------说明--------------------------
# 迭代器学习，包括如何自己建立一个迭代器对象
# ---------------------------------------------------

# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#
# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象：
# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
# 直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
from collections import Iterable


# print("列表list:", type([]), isinstance([], Iterable))
# print("字典dict:", type({}), isinstance({}, Iterable))
# print("元组tuple:", type(()), isinstance((), Iterable))
# print("集合set:", type(set()), isinstance(set(), Iterable))
# print("数字int:", type((1)), isinstance((1), Iterable))
# print("元组tuple:", type((1,)), isinstance((1,), Iterable))
# print("字符串str:", type("123"), isinstance("123", Iterable))

def printInfo(name: str, instance, judgeType=Iterable):
    print(name, type(instance), "是否是可迭代类型:{0}".format(isinstance(instance, judgeType)))


printInfo("列表list:", [])
printInfo("字典dict:", {})
printInfo("元组tuple:", ())
printInfo("集合set:", set())
printInfo("数字int:", (1))
printInfo("元组tuple:", (1,))
printInfo("字符串str:", "123")

generatorInstance = (x for x in range(10))
printInfo("生成器：", generatorInstance)
# 也就是说按照java的面向对象来可以理解 生成器实现了迭代器Iterator的可迭代接口Iterable
# 我是这么理解和猜测的，不代表实际py就是这样，需要后期验证反复理解。


# 小结
#
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的，
items = (1, 2, 3)
lists_Iterator = iter(items)
while True:
    item = next(lists_Iterator)
    print(item)
# 首先获得Iterator对象:
# it = iter([1, 2, 3, 4, 5])
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(it)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break
