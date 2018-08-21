#!/bin/bash
####################################################
#
# File Name: demo1.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年07月05日 星期三 14时17分43秒
###-----------------说明-------------------------###
#                                                   
####################################################
dirs=$1
if [ -z $dirs ];then
    dirs='./'
fi

dirs="${dirs}"
#cho "./*.sh"
#echo "文件路径:" $dirs
for file in $( find $dirs -name "*.sh")
    do
        echo $file
    done


