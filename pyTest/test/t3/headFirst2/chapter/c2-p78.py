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
import random

list1 = list(range(1, 10))
print(list1)
for item in list1:
    print(item)
list2 = list(list1[1:10:2])
list2.append("h")
list2.append('韩旭')
print(list2)
# print(''.join(list2))

listabc = ['a', 'b', 'c']
list2.extend(listabc)
fountText = input("请输入要查找的数字[a-z]");
log = "数字{0},是否在范围内：  [{1}]"
if fountText in list2:
    log = log.format(fountText, '是')
else:
    log = log.format(fountText, "否")
print(log)

print(list2)

# hi,iam hello. hanxu,jjj  -> hello, i am hanxu.
listhello = ['hi', ',', 'i', 'am', ' ', 'hello', '.', ' ', 'hanxu', 'jjj']
print("init:", listhello)
for item in listhello[0:1:1]:
    listhello.remove(item)
listhello.insert(0, listhello.pop(4))

movieli = ['a', 'b', 'c']

movieli.append(3)
sss = list(range(1, 3, 1))
movieli.extend(sss)
for item in range(1, 2 * len(movieli), 2):
    year = random.randint(1900, 1999)
    movieli.insert(item, year)
print(movieli)
type_movie = isinstance(movieli, list)
print(type_movie)
