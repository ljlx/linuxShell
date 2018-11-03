#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: 2.ipy-help.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-11-3-下午7:55
# ---------------------说明--------------------------
# ip模块实用工具.
# ---------------------------------------------------

from IPy import IP

homeip = IP('10.193.1.0/24')

print(len(homeip))
for item in homeip:
    # print(item)
    item.len()

print(homeip.broadcast())
print(homeip.get_mac())
print(homeip.net())
print(homeip.netmask())
print(homeip.reverseName())
print(homeip.reverseNames())
print(homeip.int())
print(homeip.strBin())
print(homeip.iptype())
print(IP('10.193.1.250').make_net('255.255.255.0'))
print(IP('10.193.1.250/255.255.255.0', make_net=True))
# want == 0 / None        don't return anything    1.2.3.0
# want == 1               /prefix                  1.2.3.0/24
# want == 2               /netmask                 1.2.3.0/255.255.255.0
# want == 3               -lastip                  1.2.3.0-1.2.3.255
for itemNormal in range(4):
    print(IP('10.193.1.0/24').strNormal(itemNormal))

subnet1 = IP('10.193.1.0/24')
subnet2 = IP('10.193.0.0/16')
iphost = IP('10.193.1.220')
notiphost = IP('10.0.0.0/24')

print(subnet1 < subnet2)
print(subnet2 < subnet1)
print(subnet1 == subnet2)
print(('10.193.1.2' in subnet1))
print(subnet1.overlaps(subnet2))
print(subnet2.overlaps(subnet1))
# overlaps 判断两个网段时候存在重叠,1:是,
print(iphost.len())
print(notiphost.len())
inputip = input('输入一个ip(段)地址:')

userip = IP(inputip)
print(userip)
if userip.len() > 1:
    print("是一个网络地址%s" % userip.netmask())
else:
    print("是一个ip地址:%s" % userip.iptype())
    print("是一个ip地址:%s" % userip.reverseNames())
