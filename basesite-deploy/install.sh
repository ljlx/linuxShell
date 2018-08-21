#!/bin/bash
####################################################
#
# File Name: install.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年01月11日 星期四 14时59分34秒
###-----------------说明-------------------------###
# 以root用户执行安装mysite ,或者能为这个脚本开一些sudo 的权限                                             
# 前提是先安装了tomcat和maven到了home目录,
# 
####################################################
#先创建主要的用户组website,其他的用户组件创建相应用户时,需要添加这个组进去
UserName=website
installDir=/home/website
initScriptName=init.sh
initUserDir=$installDir/installScript/config/users
#mkdir sources
#mkdir tomcat

initGroup(){
    groupadd website
    
}

#根据user,去对应的用户初始化目录去拷贝shell文件到家目录,并设置shell环境变量,
#将用户家目录所属组改为当前脚本用户,设置chmod:750,结束后设置740
#将初始脚本全部拷贝进去,设置相应的用户组权限,然后以这个用户执行脚本
initUser(){
  local user=$1;
  local initScr="$initUserDir/$user/$initScriptName";
  echo debug:"开始初始化用户[$user]自定义脚本:$initScr";
  sudo chown $user:$UserName ;
  sudo chmod g+w /home/$user ;
    echo $initScr
            echo /home/$user/
    #cp -r $initScr/* /home/$user/ ;
  #su - $user -c "$(initUser)";

  
#                  if [[ -x $initScr ]];then
#                     $initScr;

                      #./*.sh 和 /xx/xx.sh 要求执行的脚本必须有执行权限,而bash xx.sh 不要求脚本文件有执行文件,有点危险. 这3种方式都是将当前shell环境拷贝并fore新shell
                      #. xx.sh 或者 source xx.sh 不是新开(fork)一个进程来执行.是用当前shell环境执行,当前shell环境的变量可能会被这个脚本修改掉
#                 fi 
#   userName=$1
#   shellDir=$2 
#1.创建用户.把shell文件夹的初始脚本复制进去,
#2.如果存在init.sh,则执行


#    useradd mysite -G website
    
#   useradd maven -G website
#   useradd tomcat -G website
}

createUser(){
#        echo $initUserDir;
        if [[ -d $initUserDir ]];then
             local index=0;
             for itemUser in `ls $initUserDir/`
               do
                  sudo useradd $itemUser;
                  local addres=$?;
                  #需要使用创建的这个用户执行这个初始化脚本,防止越权
                  $(initUser $itemUser);
                  if [[ $? != 0  &&  $addres == 0 ]]; then
                    echo "warn: create and call user[$itemUser],init.sh has errors ,now del this user!";
                    #删除未初始化成功的用户,及其信箱文件和家目录
                   sudo userdel -r $itemUser;
                  fi
                   
               done
            
         return 0;
        fi
       return 1;
#        initUser mysite 
}

createUser
