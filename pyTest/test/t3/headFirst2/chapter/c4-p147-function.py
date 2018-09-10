#!/usr/bin/python3
#coding=utf-8
#--------------------------------------------------
# File Name: c4-p147-function.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-10-下午9:21
#---------------------说明--------------------------
# 函数的使用。
#---------------------------------------------------

def getUser(id,name):
    """
    这是python的文档注释方式，类似javadoc，不过不是在方法签名定义的头部
    :param id: id信息
    :param name: name信息
    :return: log信息凭借
    """
    id+=1;
    name+=":function"
    log="id-{0},name-{1}".format(id,name)
    return log

def search4vowels(word:str) -> set:
    """查找元音"""
    vowels=set('aeiou')
    # 取交集
    return vowels.intersection(word)


def search4vowels2(phrase:str):
    return search4text(phrase);

def search4text(phrase:str,text:str='aeiou')->set:
    """在text中查找phrase中存在的字符(取集合的交集)"""
    return set(text).intersection(set(phrase));

print(search4vowels(input("test:")))
print(search4vowels2(input("test2:")))
print(search4text("helloworld"))
print(search4text("helloworld","aeiou"))
print(search4text(text="aeiou",phrase="helloworld"))
#
#
#
#
# print(getUser(1,"hanxu"))h
# fourcom="5&1"
# # 3 * 2^2
# result=eval(fourcom)
# print(result)

