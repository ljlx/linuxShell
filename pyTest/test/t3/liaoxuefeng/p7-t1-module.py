#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: p7-t1-module.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-21-下午1:19
# ---------------------说明--------------------------
# module测试
# ---------------------------------------------------

import sys

# 模块搜索路径
print(sys.path)

# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块.
# 搜索路径存放在sys模块的path变量中

# 添加自己的模块路径
# 方法一:
sys.path.append("./tmp/")


# 这种方法是在运行时修改，运行结束后失效。
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

def test():
    print("程序参数:{0}".format(sys.argv))


if __name__ == '__main__':
    print(__name__)
    test()
