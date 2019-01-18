#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: p5-3-range.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-11-下午10:47
# ---------------------说明--------------------------
# 列表生成式和generator生成器
# ---------------------------------------------------
userIdList = list(range(1, 10));
print(userIdList)
# 但是如何生成id经过特殊规则计算的迭代值呢？ 比如列表每个元素都是2的倍数。
userIdList2 = [item * 2 for item in range(1, 10)]
print(userIdList2)


# 可以，很强大了，但是能经过一个函数计算返回值吗
def _2nj1(x):
    return 2 * x + 1


userIdList3 = [_2nj1(item) for item in range(1, 10) if item % 2 == 0]
print(userIdList3)

# Question？ 用一行代码实现 ABC三个字母的所有排序组合
userIdList4 = [item + item2 for item2 in "ABC" for item in list("ABC")]
print(userIdList4)


def _jj():
    return range(1, 9)


userIdList5 = ["{0}*{1}={2}".format(item, item2, item * item2) for item2 in _jj() for item in _jj()]
print(userIdList5)

import os

homedir = [itemDir for itemDir in os.listdir()]
print(type(homedir), homedir)

# 列表生成式也可以用来使用两个变量来访问字典

d = {'x': 'A', 'y': 'B', 'z': 'C'}
dictREsu = [k + '=' + v for k, v in d.items()]
print(dictREsu)

# 把所有字符to小写

L = ['Hello', 'World', 'IBM', 'Apple', 234]
lowchar = [s.lower() for s in L if isinstance(s, str)]
print(lowchar)

# -----------分割线-----------------------
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000
# 总结由于上面的列表生成式会直接创建整个完整的列表，假如只有之前的元素会被使用，那么列表的后面元素就白白占用内存空间了
# 因此可以把后续列表元素的创建方法保存起来，在需要那么多元素的时候 在创建，所谓的边用边创建。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

listGen = (_2nj1(item) for item in range(1, 10) if item % 2 == 0)
print(listGen)

for item in listGen:
    print(item)
# 继续使用已经用尽的生成器会抛出，StopIteration异常
try:
    print(next(listGen))
    print("测试失败")
except:
    print("测试成功")


def fub(max: int):
    count, lastnum, curnum = 0, 0, 1
    # listfub = []
    while count < max:
        # listfub.append(lastnum)
        # 就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        yield lastnum
        # 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，
        # 遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
        # 再次执行时从上次返回的yield语句处继续执行
        lastnum, curnum = curnum, lastnum + curnum
        # tuple1=(curnum, lastnum + curnum)
        # print(tuple1)
        count += 1
    # TODO throw e exception
    return "done"


listiduser9 = fub(10)
print(listiduser9, next(listiduser9))

for item in listiduser9:
    print(item)
try:
    print(next(listiduser9))
except StopIteration as e:
    print(e.value)


def testGenerator():
    print("begin")
    yield "1"
    print("step..1")
    yield "2"
    print("step..2")
    yield "3"
    print("step..3")
    return "end"


test11 = testGenerator()
while True:
    try:
        next(test11)
    except StopIteration as e:
        print(e.value)
        if e.value == "end":
            break


# test 杨辉三角
# def triangles():
#     L = [1]
#     yield L
#     while True:
#         yield L
#         maxIndex = len(L) - 1
#         k = [L[i] + L[i + 1] for i in range(maxIndex)]
        L = [1] + k + [1]
# 2nd: i=range(1-1=0);k=[];L=[1]+[]+[1]
# 3rd: i=range(2-1=1)=0;k=[1+1=2];L=[1]+[2]+[1]
# 4th: i=range(3-1=2)=0,1;k=[3,3];L=[1]+[3,3]+[1]

# print(next(triangles()))
# print(next(triangles()))
#
# print(next(triangles()))
# print(next(triangles()))
