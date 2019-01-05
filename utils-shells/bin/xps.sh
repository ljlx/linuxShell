#!/bin/bash
#--------------------------------------------------
# File Name: xps.sh
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2018-12-29 下午6:51
#---------------------说明--------------------------
#
#---------------------------------------------------

# ps -f -p


function regexPid(){
    args=$@
#    echo $args
    echo $(ps aux|grep -E $args |grep -v grep |grep -v xps.sh |awk '{print $2}')
}

case $1 in
*)
    args=$@
    PID=$(regexPid $args)
    if [[ -n $PID ]]; then
        ps -F -p $PID
      else
        echo "未查询到参数正则表达式: $args"
    fi

   ;;
esac