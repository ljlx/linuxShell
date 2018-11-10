#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: SquareSpiral1.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2018-11-9-上午9:14
# ---------------------说明--------------------------
# 第一个海龟程序
# ---------------------------------------------------
import turtle

t = turtle.Pen()
for x in range(10000):
    t.forward(10 * x)
    if x > 15:
        t.left(45)
    elif x < 15:
        t.left(90)
# TODO 说明信息,一般是需要在未来抽时间修正这里的问题的.
