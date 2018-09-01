#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-09-01 下午5:55
# ---------------------说明--------------------------
# dict操作
# ---------------------------------------------------
# 先使用初始化，后面在动态扩张i，o，u的统计信息
# vowels={}
vowels = ['a', 'e', 'i', 'o', 'u']
# found = {'o': 10, 'u': 10}
# found['o'] = 0
# found['u'] = 0
found = {}
# found.setdefault('i', 0)
# found.setdefault('e', 0)
# found.setdefault('a', 0)
isstop = False
while not isstop:
    text = input("请输入待测试的值:")
    # 输入exit则退出程序
    if "exit".__eq__(text):
        isstop = True
        break
    for item in list(text):
        if (item in vowels):
            found.setdefault(item, 0)
            found[item] += 1
            print("找到一个元音：" + item)
log = "volwel:{0}, counts:{1}"
# 打印统计结果
for itemkey, itemvalue in sorted(found.items()):
    print(log.format(itemkey, itemvalue))
