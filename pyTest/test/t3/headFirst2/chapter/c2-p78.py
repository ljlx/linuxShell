#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: c2-p78.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-8-26-下午11:32
# ---------------------说明--------------------------
# range 列表，操作
# ---------------------------------------------------

list1 = list(range(1, 10))
print(list1)
for item in list1:
    print(item)
list2 = list1[1:10:2]
print(list2)
print(''.join(list2))
