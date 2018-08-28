#!/usr/bin/python3
#coding=utf-8
#--------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-05-24 上午10:51
#---------------------说明--------------------------
#  
#---------------------------------------------------

"""
List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号([])之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
string、list和tuple都属于sequence（序列）。
可以把字符串看作一种特殊的元组。

列表截取的语法格式如下
"""
list1=['abc',123,123.123,True,False,"你好哇"];
anotherList=['def'];
tuple1=('i am a tuple',12334,222,True,False);
print(list1);

print(anotherList);
print(tuple1);

for i in list1:
    print (i);
    anotherList.append(i);
    #tuple1.append(i);
for i in tuple1:
    anotherList.append(i);

print(anotherList);

#tuple1[0]='sfadf';

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

# create a set
emetySet=set();
valSet={'123',123,True,False};
print(emetySet);
#emetySet.append("asdf",567);
print(emetySet);
print(valSet);

if('123' in valSet):
    print("valset has 123")
else:
    print("not has 123");

valSet2={'456',123,True,False};

#集合的交集
resul3=(valSet & valSet2);
print(resul3);

#集合的差集
resul4=(valSet - valSet2);
print(resul4);

#集合的并集
resul5=(valSet | valSet2);
print(resul5);

#集合的不同时存在的元素
resul6=(valSet ^ valSet2);
print(resul6);


























