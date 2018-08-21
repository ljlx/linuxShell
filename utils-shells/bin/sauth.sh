#!/bin/bash
####################################################
# File Name: sauth.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年06月26日 星期一 09时48分40秒
####################################################

currSh=$0
index=0
arg0=$0
allarg=$*
allarg2=$@
allargCount=$#
pid=$$
#echo $pid
#ls -l
#wget https://www.thesunboy.com
#lastPid=$!

#if [[ $lastPid -eq 0 ]];then

#echo suce ss $lastPid
#fi

if [[ allargCount -gt 0 ]];then
    echo "allargCount:"$allargCount
fi

for sh_file in `find ./ -name "*.sh"`
    do
       isSh="false" 
         if [ ! -x $sh_file ]; then
         #取不可执行的sh文件进行设置权限位,暂时先不管这个文件的原有权限什么情况.现在只把他设置成754
         chmod 754 $sh_file; 
         
         #result=$(($?==0?200:500))
        [ $? == 0 ] && result="成功" || result="失败"
        
        echo "设置文件["$sh_file"]权限为754" $result
         
         fi
#        else
        
        #需要使用pwd等手段结合$0 过滤掉目录 如果是sh -c command arg ..$0会是参数arg的值
# echo -e '\e[1;15m' $index ':' $sh_file '\e[1;0m' '是否是可执行文件:' $isSh;
#       if
            
#       fi

    index=$(($index + 1))
    done
