#!/usr/bin/python3
# -*- coding: utf-8 -*-
#--------------------------------------------------
# File Name: p9-t4-type.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2018-11-11-下午12:45
#---------------------说明--------------------------
# 动态创建类,以及类的本质
#---------------------------------------------------
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
#
# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
#
# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数


def testmethod1():
    print('我是类的动态方法')

type()




