#!/bin/bash
####################################################
#
# File Name: tomcat.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年11月10日 星期五 15时16分19秒
###-----------------说明-------------------------###
# 自动拷贝tomcat实例,给目录赋予权限,使用通用tomcat配置文件,支持从配置源读取配置文件                                                  
####################################################
tomcatHome="/usr/local/tomcat"
user=$1
targetDir=$tomcatHome/allServers/$1
tomcatUser="tomcat"
echo "tomcat 目录->"$targetDir
#sudo $tomcatUser -s /bin/bash
#判断该用户是否存在
    useradd $user -s /sbin/nologin > /dev/null
    if [ ! -d $targetDir ]; then
    su -l tomcat -s /bin/bash -c "mkdir -p $targetDir";
    chown $user:tomcat $targetDir
    fi
    [[ $? == 0 ]] && echo "赋权[$user]成功" || echo "赋权[$user]失败"
    
#    if [ ! -d $targetDir/ ]; then
#       mkdir -p $targetDir
#   fi

    if [ -d $targetDir/ ]; then
        cp -R $tomcatHome/tomcat/. $targetDir/. > /dev/null
        [[ $? == 0 ]] && echo "拷贝tomcat目录[$targetDir]成功" || echo "拷贝tomcat到目标目录失败>>$targetDir"
        chown -R $user:$tomcatUser $targetDir

        [[ $? == 0 ]] && echo "设置tomcat目录[$targetDir]权限成功" || echo "设置tomcat目录权限失败>>$targetDir"
    fi
