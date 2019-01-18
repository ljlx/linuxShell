#!/usr/bin/python3
# -- coding: utf-8 --
# --------------------------------------------------
# File Name: p6-t6-higherFun-partialFun.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-10-27-下午5:27
# ---------------------说明--------------------------
# 偏函数, 是个好东西啊.类似java,我经常实现一个大函数拆分成几个不同签名的小函数
# ---------------------------------------------------


def test(*text: str, **kargs):
    """

    :param text:
    :param kargs:
    :return:
    """
    targetText = "".join(text)

    startIndex = kargs.get("startIndex")
    endIndex = kargs.get("endIndex")
    buJin = kargs.get("buJin")
    return targetText[startIndex:endIndex:buJin]


print(test("abcdefg", "hijk", startIndex=0, endIndex=3, buJin=1))

kw = {"startIndedefx": 1, "endIndex": 3, "buJin": 1}
print(test("abcdefg", **kw))


def test1(*text: str, startIndex: int = 0, endIndex: int = 5):
    return test("".join(text), startIndex=startIndex, endIndex=endIndex, buJin=1)


print(test("helloworld"))
# 注意python不支持多函数名,不同参数签名的写法.
# 以上就是java版的写法,使用同方法名,参数签名不同的方式实现来实现方法重载
# 而python不需要这么麻烦的操作.
# 对于同类型,参数个数不一样 . py使用*args-可变长参数实现.
# 对于不同类型,参数个数不一样,py使用**kargs-关键字参数.字典实现,key-value形式
# py方法签名支持默认值.

# 另外就是本节重点学习的偏函数了.,他可以实现更优雅的函数重载方案.

# 当函数的参数个数太多，需要简化时，
# .使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值）
# ，返回一个新的函数，调用这个新函数会更简单。
import functools

# 起始位置为0,步进为,从末尾到前,按1个字符为间隔
test2 = functools.partial(test, 'hanxu', buJin=-1)

print(test2('hello', 'word', 'python'))

# print('hellowordllllll'[100::-1])
