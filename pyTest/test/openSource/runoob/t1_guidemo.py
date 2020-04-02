#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#--------------------------------------------------
# File Name: 1.guidemo.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-10-下午12:59
#---------------------说明--------------------------
# 来自runoob网站的gui示例demo
# http://www.runoob.com/python/python-gui-tkinter.html
#---------------------------------------------------
# sudo apt-get install python3-tk*
from tkinter import *
import os
# 导入 Tkinter 库
root = Tk()
# 创建窗口对象的背景色
# 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)
#  创建两个列表组件
# listb2 = Listbox(root)
homedir=os.listdir("/home/hanxu/")
for item in homedir:
    # 第一个小部件插入数据
    listb.insert(0,item)

# for item in movie:
#     第二个小部件插入数据
    # listb2.insert(0,item)
#
listb.pack()
# 将小部件放置到主窗口中
# listb2.pack()
root.mainloop()

# 进入消息循环
