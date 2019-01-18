#!/usr/bin/python3
# -- coding: utf-8 --
# --------------------------------------------------
# File Name: p6-t4-higherFunction-returnFun.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-10-27-下午1:22
# ---------------------说明--------------------------
# 返回函数的使用
# ---------------------------------------------------


def fastSum(*args) -> int:
    """
    输入若干数,返回计算的和
    :param args:
    :return: 返回和
    """
    sum = 0
    for i in args:
        sum += i
    return sum


print(fastSum(1, 2, 3, 4, 5))


def lazySum(*args):
    def sum():
        sum = 0
        for i in args:
            sum += i
        return sum

    return sum


sumfun = lazySum(1, 2, 3, 4)
print(sumfun())
# 还真是奇怪的语法啊,呵不是嘛,,(/xk手动笑哭)
print(lazySum(1, 2, 3, 4)())


# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力

# 这个和java的匿名内部类是同出一辙.刚开始觉得好像很牛逼..
# 用的久了.就会觉得代码太难看了,不直观不易读,被lamada取代

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
# 我猜测是返回各个i乘积的匿名函数
print(f1())
print(f2())
print(f3())


# 然而结果出乎预料,居然都是返回9, 看来由于创建的这些匿名函数,都保持的是原有i的引用
# 而不是一个i的拷贝,这个问题需要了解下python有没有类似java的值类型和引用类型


# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 所以说就可以理解java的在匿名内部类中强制要求是final类型的,要求至少外部不能在修改了.

# ----------start----------凡事都有例外,这是引用改变的解决办法----------start----------
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count2():
    def finalSum(i):
        def sum():
            return i * i

        return sum

    fs = []
    for i in range(1, 4):
        fs.append(finalSum(i))
    return fs


fs = count2()
for item in fs:
    print(item())


# ----------end------------凡事都有例外,这是引用改变的解决办法----------end------------

def createCounter():
    def counter():
        def random():
            n = 1
            while True:
                n += 1
                # yield n
                return n

        return random

    return counter


# 一、在内部函数内修改外部函数局部变量的两种方法
# 1法：把外部变量变成容器或者说可变变量
def count2():
    i = [0]

    def finalSum():
        i[0] = i[0] + 1
        return i[0]
    # return lambda :(i[0]+=1)
    return finalSum

co2=count2()
print("lambda实现:",co2())
print("lambda实现:",co2())
print("lambda实现:",co2())

# 2法：在内部函数里给予外部函数局部变量nonlocal声明，让内部函数去其他领域获取这个变量
def count3():
    i = 0

    def finalSum():
        nonlocal i
        i += 1
        return i

    return finalSum


# 二、在内部函数内修改全局变量
def count4():
    global i
    i = 0

    def finalSum():
        global i
        i += 1
        return i

    return finalSum


counterA = count4()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = count4()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
