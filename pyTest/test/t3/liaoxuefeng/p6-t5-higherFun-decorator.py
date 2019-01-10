#!/usr/bin/python3
# -- coding: utf-8 --
# --------------------------------------------------
# File Name: p6-t5-higherFun-decorator.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-10-27-下午3:24
# ---------------------说明--------------------------
# 装饰器,类似与java的动态代理,spring的aop功能
# ---------------------------------------------------

import datetime


class Cat(object):

    def run(self):
        print("Cat我开始跑步那...")

    def eat(self):
        print('Cat我开始吃饭那')


cat1 = Cat()

cat1.run()
cat1.eat()
# 由于py的函数可以像变量一样进行使用.so...
cat_method_run = cat1.run
catrunname = cat_method_run.__name__
print(catrunname)


# 既然能拿到方法的名字. 那么..
def logtime(func):
    def wrapper(*args, **kwargs):
        # proxy_resu = func(args, kwargs)
        funcname = func.__name__
        print("time:{},method:{}".format(datetime.datetime.today(), funcname))
        # proxy_resu = func(args,kwargs)
        proxy_resu = func(*args, **kwargs)
        print('at {} call method {}. end! ,and result is:{}'.format(datetime.datetime.today(), funcname, proxy_resu))
        return proxy_resu

    return wrapper


# 现在我需要哦在两个方法执行的前后进行动态代理.


# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
#
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
#
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：


def log(text: str):
    def logtime(func):
        def wrapper(*args, **kwargs):
            # proxy_resu = func(args, kwargs)

            funcname = func.__name__
            print(text.format(datetime.datetime.today(), funcname))
            # proxy_resu = func(args,kwargs)
            proxy_resu = func(*args, **kwargs)
            print('at {} call method {}. end! ,and result is:{}'.format(datetime.datetime.today(), funcname, proxy_resu))
            return proxy_resu

        return wrapper

    return logtime


class Dog(object):

    @log("at {} call method {}. startting... ")
    def run(self):
        print("run==>do some thing")
        return "跑步"

    @log("at {} call method {}. startting... ")
    def eat(self):
        print('eat==>do some thing')
        return "吃饭"


dog1 = Dog()

# logtime(dog1.run)()

dog1.eat()

wrapperLog = log("at {} call method {}. startting...")

# 参考原文
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000

# 以上两种decorator的定义都没有问题，但还差最后一步。
# 因为我们讲了函数也是对象，它有__name__等属性，
# 但你去看经过decorator装饰之后的函数，
# 它们的__name__已经从原来的'now'变成了'wrapper'：

wapperFunc = wrapperLog(cat1.run)
print(wapperFunc.__name__)


# 因为返回的那个wrapper()函数名字就是'wrapper'，
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错

def logtimeNew(func):
    def wrapper(*args, **kwargs):
        # proxy_resu = func(args, kwargs)
        funcname = func.__name__
        print("{}{}".format(datetime.datetime.today(), funcname))
        # proxy_resu = func(args,kwargs)
        proxy_resu = func(*args, **kwargs)
        print('at {} call method {}. end! ,and result is:{}'.format(datetime.datetime.today(), funcname, proxy_resu))
        return proxy_resu

    wrapper.__name__ = "proxy$" + func.__name__
    return wrapper


wapperFunc = logtimeNew(cat1.run)
print(wapperFunc.__name__)

# 不需要编写wrapper.__name__ = func.__name__这样的代码，
# Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：


# ----------start----------好了,玩耍结束,此处为终极代理方案----------start----------

import functools


def logfunc(func):
    @functools.wraps(func)
    def wapper(*args, **kwargss):
        funcName = func.__name__
        print('start call {}'.format(funcName))
        funcResult = func(*args, **kwargss)
        print('end call {},result is {}.'.format(funcName, funcResult))
        return funcResult

    return wapper


class SuperMan(object):

    @logfunc
    def fly(self):
        print("fly==>do some thing")
        return "飞翔"

    @logfunc
    def hit(self):
        print('hit==>do some thing')
        return "打击"


hanxu = SuperMan()
hanxu.fly()
hanxu.hit()
hanxufly = hanxu.fly
print(hanxu.hit)
# ----------end------------好了,玩耍结束,此处为终极代理方案----------end------------
