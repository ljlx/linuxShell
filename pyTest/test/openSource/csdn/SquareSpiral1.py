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


def test1():
    t = turtle.Pen()
    t.speed(10)
    i = 0
    limiti = 2
    for x in range(300):
        if i < limiti:
            t.forward(60)
            t.left(120 + x)
        elif (i == limiti):
            i = 0
            t.forward(120)
            t.left(60 + x)
        i += 1

    print("")


# TODO 说明信息,一般是需要在未来抽时间修正这里的问题的.

def test2():
    t = turtle.Pen()
    t.speed(20)
    for i in range(1000):  # range(100)[1:1000:1]:
        t.forward(100)
        # t.right(8)
        # if i % 2 == 0:
        #     t.left(90)
        # else:
        t.left(91)
2

def test3():
    turtle1 = turtle.Pen()
    turtle1.color("purple")
    turtle1.pensize(5)
    turtle1.goto(0, 0)
    turtle1.speed(10)
    for i in range(5):
        turtle1.forward(100)
        turtle1.right(144)
    turtle1.up()
    turtle1.forward(100)
    turtle1.goto(-150, -120)
    turtle1.color("red")


test3()
print('end')
