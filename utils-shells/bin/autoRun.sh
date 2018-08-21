#!/bin/bash
####################################################
#
# File Name: autoRun.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年12月01日 星期五 19时51分37秒
###-----------------说明-------------------------###
#                 开启自启的功能脚本 
# 后续需要增加的功能:1.可以指定动作行为对某一个服务的操作
####################################################
initDir=$1
echo $realpath
if [ -d $initDir ];then
    echo "自动启动脚本的目录是:$initDir----[成功]"
    #取参数目录所在的父目录的绝对路径
   realpath_parent=$(cd "$(dirname $initDir)"; pwd);
   dirName=basename $1 ;
   echo 'dir:'$dirName
   
   echo "real: "$realpath_parent 
   else
    echo "该自动启动脚本目录不存在:$initDir"
fi
echo $realpath_parent
