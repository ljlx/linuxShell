#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p9-t4-type.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2018-11-11-下午12:45
# ---------------------说明--------------------------
# 动态创建类,以及类的本质
# ---------------------------------------------------
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
#
# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
#
# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数

class Hello(object):
    def dohello(self, name='world'):
        print('hello,%s.' % name)


h = Hello()
h.dohello()
print(type(h))
print(type(Hello))


def testmethod1(self, age=12):
    self.name = 'name'
    self.age = age
    print('我是类的动态方法,创建了name和age变量')


def testmethod2(self):
    print('我是类的动态方法{},{}'.format(self.age, self.name))


Hallo = type('Hallo', (object,), dict(hello=testmethod1, hello2=testmethod2))
hallo1 = Hallo()
hallo1.hello(24)
hallo1.hello2()
