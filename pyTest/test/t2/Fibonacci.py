#!/usr/bin/python3
#coding=utf-8
#--------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-06-01 下午3:17
#---------------------说明--------------------------
#   斐波纳契数列
#---------------------------------------------------
a, b = 0, 1
while b < 1000000:
    print(b,end='-');
    a, b = b, a+b;

    # a=b;
    # b=a+b;


