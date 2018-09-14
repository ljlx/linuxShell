#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: p6-t1-higherFunction.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-13-下午9:19
# ---------------------说明--------------------------
# 高阶函数的使用
# 函数本身也可以赋值给变量，即：变量可以指向函数
# ---------------------------------------------------


from os import uname


def add(a: int, b: int) -> int:
    return 2 * a + b


print(add(3, 4))
print(add)
f = add
print(f)
print(f(3, 4))
add = 123
try:
    print(add(3, 4))
except Exception as e:
    print(e)
    pass

print(f(3, 4))

# 注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10
# 我这里以os.uname为例子
print(uname())
myuname = uname
print(uname, myuname)
uname = "hanxu"
print(myuname())
try:
    print(uname())
except Exception as e:
    print(e)
    pass


# import os
#
# os.utime = 123

def add2(a: int, b: int, f) -> int:
    return f(a, b) + f(a, b);


add = add2
print(add(2, 3, f))
