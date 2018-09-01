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
vowels = {'o': 10, 'u': 10}
vowels['o'] = 0
vowels['u'] = 0
vowels.setdefault('i', 0)
vowels.setdefault('e', 0)
vowels.setdefault('a', 0)
isstop = False
while not isstop:
    text = input("请输入待测试的值:")
    # 输入exit则退出程序
    if "exit".__eq__(text):
        isstop = True
        break
    for item in list(text):
        if (item in vowels):
            vowels[item] += 1
            print("找到一个元音：" + item)
log = "volwel:{0}, counts:{1}"
# 打印统计结果
for itemkey, itemvalue in sorted(vowels.items()):
    print(log.format(itemkey, itemvalue))
