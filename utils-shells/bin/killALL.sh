#!/bin/bash
####################################################
#
# File Name: killALL.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年01月10日 星期三 20时51分11秒
###-----------------说明-------------------------###
#                                                   
####################################################
pname=$1
signal=$2
if [[ -z ${signal} ]]; then
    signal=15;

fi
pid=$(ps aux | grep $pname | grep -v grep | awk '{print $2}' | xargs);

echo "使用kill -${signal} 来杀死。${pid}";
#xargs
kill -${signal} ${pid}
