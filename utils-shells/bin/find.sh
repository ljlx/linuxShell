#!/bin/bash
####################################################
#
# File Name: find.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年09月06日 星期三 22时00分58秒
###-----------------说明-------------------------###
#  ls 出 find 的执行目录结构                                                
####################################################
#path=$1
#filter=$2
#re=$(find $path -name "*$filter'*'")
#cat $re
path=$(pwd)
echo "以下路径查找" ${path}
files=$@
where
for item in ${path}
    do
    where="${where}" -name ${item}
    done
echo $where