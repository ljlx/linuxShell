#!/bin/bash
####################################################
#
# File Name: batchMd5.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年10月25日 星期三 16时00分16秒
###-----------------说明-------------------------###
#  input为一个文件集合.可以使用ls命令 ls | batchMd5.sh 作为文件夹的输出流
# 用于查看一个文件夹下的所有md5信息
####################################################

files=$1

#echo $files

if [[ -d $files ]];then
#for file in ``
#  else 
    for file in `ls $files`
    do
        file=$files/$file;
        if [[ -f $file ]];then
        /usr/bin/md5sum $file;
        fi
#echo $file md5=$((md5sum $file))
#       echo "is not folder"
    done

fi
