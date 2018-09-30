#!/bin/bash
#--------------------------------------------------
# File Name: ${FILE_NAME}
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-05-18 下午12:36
#---------------------说明--------------------------
#  安装dnsmasq配置信息
#---------------------------------------------------

dnsconfFileName="dnsmasq.hanxu.conf"

sudo echo "conf-file=/etc/${dnsconfFileName}" >> /etc/dnsmasq.more.conf
sudo cp -r ./dnsmasq_hanxu.d /etc/



