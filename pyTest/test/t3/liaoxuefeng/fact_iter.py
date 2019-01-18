#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: fact_iter.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-11-下午12:33
# ---------------------说明--------------------------
# 尾递归，避免栈溢出，但是大多数语言包括py都没有实现其优化
# ---------------------------------------------------

def fact(n: int):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    print("num:{},product:{}".format(num, product))
    return fact_iter(num - 1, num * product)


inti = int(input("num:"))
print(fact(inti))
