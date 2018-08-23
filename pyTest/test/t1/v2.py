#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding=utf-8
# --------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-08-23 下午4:29
# ---------------------说明--------------------------
#  
# ---------------------------------------------------

list = ['a', 'b', 'c'];

str1 = "ab\r\ncd";
print(str1);

for item in list:
    print("original", item);
    print('ord:', ord(item));
    print('chr:', chr(ord(item)));
    # python3 不支持unichr， 只需要chr就可以转了.
    print('unichr:', unichr(ord(item)));
print(u'我爱你');
namejj = u'我爱';
print(namejj);
namejjj = namejj.encode('utf-8');

list1 = ["a", "b", "我", "爱", "你"];
for item in list1:
    print(item)
    # charcode = ord(item);
    # print(unichr(charcode));
print(unichr(20013));

print(chr(82));
