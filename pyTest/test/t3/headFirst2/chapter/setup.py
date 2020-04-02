#!/usr/bin/python3
#coding=utf-8
#--------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-09-16 下午12:08
#---------------------说明--------------------------
# 发布包模块
#---------------------------------------------------
# 要发布一个python模块,需要将要发布的py文件置于一个目录下,还需要使用setup.py,和readme.txt文件
# 使用python3.4 版本以上提供的setuptools模块来安装到site-package

# from distutils.core import setup
# from distutils.command.install import install

# from distutils.core import setup
from setuptools import setup,find_packages
# import t3.liaoxuefeng.fact_iter
setup(
    name="headfirstDemo",
    version="1.0",
    description="this is test for headfirstDemo to package",
    author="hanxu",
    author_email="hx940929@qq.com",
    url="https://www.thesunboy.com",

)
