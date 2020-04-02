#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: c3-p132.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-6-下午10:53
# ---------------------说明--------------------------
# 元组和集合的操作
# ---------------------------------------------------
tuple1 = ("1", "2", "3", "1")
tuple3 = tuple("12348937455")
tuple2 = (1,)
# 元组的语法类型是以逗号，来区分的，如果在一个元素的情况下不加逗号就会变成单个字符串或数字
char1 = ("1")
num1 = (1)

print("第一个元组类型", type(tuple1));
print(tuple2, type(tuple2))
print(tuple3)
print(char1, type(char1))
print(num1, type(num1))

jj = tuple1.count("1")
print(jj)
print(tuple1)
print(tuple1[2])
# 元素是不可变,顺序的数据类型

# python的集合相当于java里的set

set1 = {'a', 'b', 'a', 'b', 'c', 'd', 'e', 'c', 'd', 'e', 'a', 'b', 'c', 'a', 'b', 'c', 'd', 'e', 'd', 'e'}
set2 = set("jwoiejfoaijjawoeijfawjopifwiejf")
print(set1, type(set1))
print(set2, type(set1))
# 该集合是数学意义上的集合，无序无重复，可以理解成 就是初中数学学习的集合操作，可以取并集交集差集
# 并集
unionSet = set1.union(set2)
# 差集
diffSet = set1.difference(set2)
# 交集
intersectSet = set1.intersection(set2)

print("并集：", unionSet)
print("差集：", diffSet)
print("交集：", intersectSet)
# set1 = 差集+交集。
