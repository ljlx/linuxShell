#!/bin/bash
####################################################
#
# File Name: isstart.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年07月04日 星期二 14时13分43秒
###-----------------说明-------------------------###
#    demo-判断某一个服务是否开启. 使用的ps 进程名的方式                                               
####################################################

localn=$0
queryName=$1
iskill=$2
echo 正在查询进程[${queryName}]是否存在,使用stop停止它.
pName=$(ps aux | grep ${queryName} | grep -v ${localn} | grep -v grep)

if [ -n "$pName" ];then
    
#    echo "进程[" $pName "]开启----Start 绿色"
# echo -e '\e[1;$33m'"进程[" $queryName "]开启----Start 绿色"'\e[0m'
     pid=$(echo ${pName} | awk '{print $2}' )
     #echo ${pName}; TODO 增加参数是否显示详细信息
     echo -e "进程pid:[$pid]-[$queryName]开启----[\e[1;32m Running\e[0m ]"
    #使用awk等工具拿到pid并显示出来
    if [[ ! -z ${iskill} && ${iskill} == 'stop' ]]; then
        echo 'kill pid '${pid}
        kill -9 ${pid}
    fi
     else

#echo "进程[" $pName "]未开启----Stop 红色色"
# echo -e "\e[1;$41m 进程[" $queryName "]未开启----Stop 红色\e[0m"
    
     echo -e "进程[${queryName}]未开启----[\e[1;31m Stop\e[0m ]"

# echo -e "\e[34m 黄色字 \e[0m" 
#    echo -e "\e[41;33m 红底黄字 \e[0m"
#    echo -e "\e[41;37m 红底白字 \e[0m" 
     
     fi
