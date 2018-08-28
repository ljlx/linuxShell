#!/usr/bin/python3
#coding=utf-8
#--------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-05-24 下午2:14
#---------------------说明--------------------------
#  #字典的使用，dictionary
"""
另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。

注意：

    1、字典是一种映射类型，它的元素是键值对。
    2、字典的关键字必须为不可变类型，且不能重复。
    3、创建空字典使用 { }。
"""
#---------------------------------------------------
dict1={};
dict1['key1']="asdflkj";
dict1['key2']="love";
dict1['key3']="you";
dict1['do']='yes';
dict1['age']=1234;
dict1['islove']=True;

print(dict1.keys());
print(dict1.values());

print(dict1['key2']);
print(dict1['islove']);

#构造函数

dict2=dict([('key1','value1'),('name','hanxu'),('age','23')]);
print(dict2);
print(dict2['name']);