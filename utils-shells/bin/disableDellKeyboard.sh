#!/bin/bash
####################################################
#
# File Name: demo1.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年09月07日 星期五 12时17分43秒
###-----------------说明-------------------------###
# 操作笔记本键盘开关状态。
####################################################
#echo "禁用笔记本键盘成功"
#echo "--used xinput [list | --list-props | --set-prop (dcevicesId,funId,status)]"

keyboardId=$(xinput list |grep "T Translated Set 2 keyboard" | awk '{print $7}' |awk -F = '{print $2}')

swith=$1
if [[ -z ${swith} ]];then
	swith=0
fi

resut=$(xinput --set-prop ${keyboardId} 142 ${swith})
