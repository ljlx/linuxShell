#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: 1.numba-jit.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-10-下午1:57
# ---------------------说明--------------------------
# 初识 numpy
# ---------------------------------------------------

# TODO python提高篇.

# https://blog.csdn.net/qq_42156420/article/details/82812180
import time

# pip3 install numba
# Successfully installed llvmlite-0.27.0 numba-0.42.0 numpy-1.15.4
from numba import jit


@jit
def emptyFun(s: int):
    s += 1;
    return s


# 确实,在使用了jit后,速度提升很大
@jit()
def foo(x, y):
    tt = time.time()
    s = 0
    for i in range(x, y):
        s += i
        # 奇怪的是使用了jit,在有这个多余的方法调用和if判断,反而速度变慢了.
        # 明白了,原来是因为调用的emptyFun函数没有加上@jit注解.@jit装饰器
        if s % 2000 == 0:
            emptyFun(s)
            print(s)
    print('Time used: {} sec'.format(time.time() - tt))
    return s


# decompile_func能将函数的代码对象反编译成ast语法树，而str_ast能直观地显示ast语法树，使用这两个工具学习Python的ast语法树是很有帮助的。

#
# print
# str_ast(decompile_func(add2))
# FunctionDef(args=arguments(args=[Name(ctx=Param(),
#                                       id='a'),
#                                  Name(ctx=Param(),
#                                       id='b')],
#                            defaults=[],
#                            kwarg=None,
#                            vararg=None),
#             body=[Return(value=BinOp(left=Name(ctx=Load(),
#                                                id='a'),
#                                      op=Add(),
#                                      right=Name(ctx=Load(),
#                                                 id='b')))],
#             decorator_list=[],
#             name='add2')

if __name__ == '__main__':
    print(foo(1, 100000000))
