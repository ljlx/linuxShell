#!/bin/bash
####################################################
#
# File Name: batchAddUser.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年07月05日 星期三 17时28分18秒
###-----------------说明-------------------------###
#                                                   
####################################################
#函数定义区
##判断第一个值是否为有效数字,如果不是就返回第二个参数的值
function defValue()
{
    echo "进入函数"
    value=$1
    defValue=$2
    echo "arg0="${value};
    echo "arg1="${defValue};

    if [[ -z ${value} ]]; then
            echo "进入判断1"
            value=${defValue}
        else
        #不为空,则判断是否为数字类型,不是数字则重置为0
        temp=$(echo ${value} | sed 's/[0-9]//g')
            if [[ -n ${temp} ]]; then
            echo  "进入判断2"
            echo ${value}
            #不是数字则重置为0 
            return ${value}
            fi
    fi
}
###函数定义区###
#read -p "请输入用户名:" userName
#read -p "请输入默认密码:" defPwd
read -p "请输入起始用户位置:" startIndex
#read -p "创建的用户量:" nums
##初始化startIndex
echo "开始参数校验------start--------"
startIndex=$(defValue ${startIndex} 0);
#nums=$(defValue $nums 10);
##初始化startIndex完成
echo "参数校验完毕------end------"
echo "startIndex==>" ${startIndex}
#echo "nums" $nums
#开始批量添加用户
if [[ ! -z $userName && ! -z $defPwd ]]; then
    echo "asdf"
fi

