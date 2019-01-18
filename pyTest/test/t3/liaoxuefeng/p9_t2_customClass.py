#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p9-t2-customClass.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2018-11-3-下午2:57
# ---------------------说明--------------------------
# 定制化类,重载预制的各种方法,比如tostring,length,slots等
# ---------------------------------------------------

class originalStudeng(object):

    def __init__(self, name):
        self.name = name


print(originalStudeng('xiaomin'))


class butifulStudent(originalStudeng):

    def __str__(self):
        return "butifulStudent:" + self.name

    def __repr__(self):
        return "debug:" + self.name

    __repr__ = __str__

    def __len__(self):
        return len(self.name)


var1 = butifulStudent('小民')

# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的

var2 = len(butifulStudent('小民'))
var3 = len(butifulStudent('jjjj'))


# ----------start----------iter使用----------start----------
# __iter__ 迭代器
#
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
#
# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            return getitem(self, item)
        if isinstance(item, slice):
            return getitem2(self, item)
        raise NotImplementedError()


def getitem(self, n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a


# 两种方法都可以,不过idea会警告[]不支持
# Fib.__getitem__ = getitem
# Fib.__getitem__ = MethodType(getitem, Fib)


fibins = Fib()

print(fibins)
for item in fibins:
    print(item)

print(fibins[10])


# 但是list有个神奇的切片方法：
# list(range(100))[5:10]
# [5, 6, 7, 8, 9]
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int
# 也可能是一个切片对象slice，所以要做判断：

def getitem2(self, n):
    # 如果是切片对象
    if isinstance(n, slice):
        start = n.start
        stop = n.stop
        if start is None:
            start = 0
        resutlist = []
        a, b = 1, 1
        for x in range(stop):
            if x >= start:
                resutlist.append(a)
            a, b = b, a + b
        return resutlist
    raise NotImplementedError()


fibinsslice = Fib()
from types import MethodType

fibinsslice.__getitem__ = MethodType(getitem2, fibinsslice)
sliceFib = fibinsslice[5:10]
print(sliceFib)

# 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
#
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
#
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
#
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
# 我的笔记:
# 相比java,用java的语言来说就是预先在object实现了若干接口,只是是个虚假的空实现来达到这个目的.
# 之类根据需要复写

# ----------end------------iter使用----------end------------


# !/usr/bin/python3.5
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==9.0.1','console_scripts','pip'
__requires__ = 'pip==9.0.1'


# load_entry_point('pip==9.0.1', 'console_scripts', 'pip')()

# if __name__ == '__main__':
#     sys.exit(
#
#         load_entry_point('pip==9.0.1', 'console_scripts', 'pip')()
#     )


# ----------start----------避免has no attribute 异常,使用getattr特殊方法----------start----------
class Student(object):

    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        print("try find a str attribute: %s" % attr)
        if attr == 'scores':
            return 99
        if attr == 'age':
            return lambda: 25


hanxu = Student('hanxu')
print("name[{}],score[{}],is {} ago.".format(hanxu.name, hanxu.scores, hanxu.age()))


# 参考
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000#2
# 总结
# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
#
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用
# __getattr__和__getattribute__区别? 调用起来感觉有点像java的反射直接使用了proxy.tostring. 内部方法循环调用造成栈溢出.
# 区别应该就是__getattr是代码显式调用不存在的属性才会触发,而attribute是所有的属性方法,比如str方法也会触发.
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if isinstance(path, classmethod):
            return Chain(self._path)
        return Chain("%s/%s" % (self._path, path))

    def __call__(self, *args, **kwargs):
        # TODO 如何取出调用的method名
        print(self._path)

    def printPath(self):
        print(self._path)


hanxuChain0 = Chain().user.list.detail.hanxu
hanxuChain0.printPath()
hanxuChain = Chain().user.list.detail
# 掉不存在的方法时,先调用了getattr,在调用了call
hanxuChain.hanxu()
hanxuChain.printPath()

# ----------end------------避免has no attribute 异常,使用getattr特殊方法----------end------------
