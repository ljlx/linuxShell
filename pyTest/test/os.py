#!/usr/bin/python3
#coding=utf-8
#--------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-05-24 下午3:32
#---------------------说明--------------------------
import os;
#如果是 posix，说明系统是 Linux；如果是 nt，则是 Windows 系统。
#go on fix bug 1
#go on fix bug 2



print(os.name);

pwd=os.getcwd();
print(pwd);
evn=os.getenv("PUB_SHELLS");

os.name;

print(evn);
print(os.uname());
print(os.getuid());

rootdir=os.listdir("/");
for i in rootdir:
    print(i);
