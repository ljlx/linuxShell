#!/bin/bash
####################################################
#
# File Name: pptpRoute.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年11月15日 星期三 21时02分41秒
###-----------------说明-------------------------###
#
####################################################
pptpdHome="/etc/ppp/"
pptpEvent="ip-up"
routeFile=$1
routeUser="route"
pptpRouteFile="$pptpdHome/autoStaticRoute/"$routeFile".route"
alias date='date "+%Y-%m-%d %H:%M:%S"'
#$pptpdServerHome
if [ -f $pptpRouteFile ];then
    echo -e "执行路由脚本>> "$pptpRouteFile", 内容如下>> \n"
    cat $pptpRouteFile
    echo -e "\n现在时间是>> "$(date)
    echo -e "路由脚本>> "$pptpRouteFile",结束,以上为路由脚本内容,下面开始执行"
#    for single in `cat $pptpRouteFile`
        while read -r single
        do
            errorMsg=$(su -l $routeUser -s /bin/bash -c "sudo $single");
            if [[ $? == 0 ]]; then
                echo "执行路由成功>>"$single
              else
                echo "执行路由失败,应该回滚之前的路由>>" $single
                echo $errorMsg
            fi
        done < $pptpRouteFile

# 不需要为每一个路由文件添加静态路由,只针对当前连接的用户建立相应的永久路由
#    for item in `ls $pptpRouteFolder/*.route`
#       do
#          routeLog=
#       done
fi
