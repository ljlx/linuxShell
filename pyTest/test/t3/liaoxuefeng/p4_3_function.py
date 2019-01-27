# !/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: p4-3-function.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-11-下午12:45
# ---------------------说明--------------------------
# function的使用，及其注意事项
# ---------------------------------------------------
# 普通函数，按照方法签名顺序设置，这叫位置参数
def test(users=[]):
    users.append("end");
    return users;


print(test(["1", "abc"]))
print(test(["jjj", "23"]))
print(test())
print(test())


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 我们把函数的参数改为可变参数：
def calc(*numbers):
    """
    可变长的参数，类似与java里面的public void ss(String... args)这种写法。
    定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，
    因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
    :param numbers:
    :return:
    """
    sum = 0
    print(type(numbers), numbers)
    for n in numbers:
        sum = sum + n * n
    return sum


calc(1, 2, 3)
tuple1 = (1, 2, 3)
list2 = [1, 2, 3]
# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

# print(calc(tuple1))
print(calc(*tuple1))
print(calc(*list2))


# 关键字参数,类似是传了一个map进来,其实就是个dict

def person(name, age, **extend):
    log = "name:{0},age:{1},extend:[{2}]".format(name, age, extend)
    print(log)


person("hanxu", 22)
person("hanxu", 22, city="wuyishang", love="jchen", sex="man")
dict1 = {"city": "wuyishang", "love": "jchen", "sex": "man"}
person("hanxu", 22, **dict1)


# 注意extend获得的dict是dict1的一份拷贝，对extend的改动不会影响到函数外的extend。

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person1(name, age, *, addr, sex=1, ishappy="goodQuestion"):
    """
    命名关键字参数
    :param addr:
    :param sex:
    :param name:
    :param age:
    :param extend:
    :return:
    """
    extend = {}
    extend["addr"] = addr
    extend["sex"] = sex
    extend["ishappy"] = ishappy
    log = "name:{0},age:{1},extend:[{2}]".format(name, age, extend)
    return log


print(person("hanxu", 22, ss=22, jj=22))
print(person1("hanxu", 22, addr="fujian"))
print(person1("hanxu", 22, addr="fujian", sex=100, ishappy="maybe"))


# 总结
# 参数组合

# 在Python中定义函数，可以用必选参数(普通方法参数)、默认参数(设置默认值)、可变参数(元组)、关键字参数(字典)和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


def product(x, *y):
    sum = x
    for item in y:
        sum *= item
    return sum


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

