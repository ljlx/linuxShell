#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: p6-t2-higherFunction-filter.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-14-下午8:59
# ---------------------说明--------------------------
# 高阶函数过滤器使用
# ---------------------------------------------------
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000
listNUm = list(range(1, 10))


def getEvenNum(x: int):
    return x % 2 == 0


# 过滤器 过滤列表, function返回true的值会保留,false的将会抛弃
evenNum = list(filter(getEvenNum, listNUm))
print(evenNum)


def not_empty(s: str) -> bool:
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, ' C', '  '])))


# 用filter求素数
# 计算素数的一个方法是埃氏筛法
# 从3开始的奇数生成器
def _odd_iter() -> object:
    """

    :rtype: object
    """
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n: int):
    """
    注意,此方法我猜测并不是一个筛选函数,它返回了一个lambda作为筛选函数,
    filter会调用被筛选的列表的next方法,返回一个列表第一个值为x的值,使其与第一个奇数n来进行模除测试x是否为素数,如果是x将作为下次迭代的n
    :param n:
    :return:
    """
    # 该lambda表达式的意识是,定义一个匿名函数,入参数是x
    # 换成java我猜应该是以下表达意思
    # new callback(n){ boolean invoke(var x){ return x % n >0; } }
    # 还是暂时不理解这个lambda表达式的x参数
    # lambda x: {print("x:[{0}],n[{1}],x%n:[{2}]".format(x, n, x % n))}
    print("n=", str(n))
    return lambda x: x % n > 0


# def _not_divisible(n: int, *x: int):
#     log = "n:[{0}],x:[{1}]".format(n, x)
#     print(log)
#     return x % n > 0


def prime():
    """
    素数生成器
    :return:
    """
    # 定死返回第一个值
    yield 2
    # 初始化奇数生成器,即返回第一个数,该数一定是一个素数
    itt = _odd_iter()
    while True:
        oddNum = next(itt)
        yield oddNum
        # 经过not_divisible过滤器,过滤itt的奇数列表,留下的是当前不能被oddnum整除的素数,但是itt剩下还有很多未被过滤的
        # itt = filter(_not_divisible(oddNum), itt)
        itt = filter(_not_divisible(oddNum), itt)


for n in prime():
    if n < 20:
        print(n);
    else:
        break


# 练习
def is_palindrome(n):
    k = str(n)
    alls = k[::-1]
    return k == k[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
