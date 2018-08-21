#!/bin/bash
####################################################
#
# File Name: install.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年02月04日 星期日 23时10分42秒
###-----------------说明-------------------------###
#  安装开发环境脚本,主要是根据参数执行其下所有 或者指定的脚本,并且创建一个良好的执行环境 供子脚本执行
####################################################
baseDir=/usr/pubShells/developEnvironment/bin/aliasAndEnv

#环境变量
myshell_BaseDir=""


if [[ ! -z ${myshell_BaseDir} && -d ${myshell_BaseDir} ]]; then
	   baseDir=${myshell_BaseDir}
fi
aliasDir=${baseDir}/aliasDir
envDir=${baseDir}/bash_env
functions=${baseDir}/function

function setalias(){
if [ -d ${aliasDir} ]; then
    for item in `ls ${aliasDir}/*.sh` ; do
    	    source ${item}
	    code=$?
	[ ${code} == 0 ] && echo "appaly alias file :"${item} || echo "error:"${code}

    done
   else
    echo "目录[${aliasDir}]不存在,不执行安装"
fi
}

function setenv(){
if [ -d ${envDir} ]; then
    for item in `ls ${envDir}/*.sh` ; do
    	    source ${item}
	    code=$?
	    echo ${code}
	[ ${code} == 0 ] && echo "appaly Env:"${item} || echo "error:"${code}
    done
    else
     echo "目录[${envDir}]不存在,不执行安装"
fi
}

function setfunction(){
if [ -d ${functions} ]; then
    for item in `ls ${functions}/*.sh` ; do
    	    source ${item}
	    code=$?
	[ ${code} == 0 ] && echo "appaly Function:"${item} || echo "error:"${code}
    done
    else
     echo "目录[${functions}]不存在,不执行安装"
fi
}
#安装环境变量别名,以及注册function
function _install_aliasAndEnv(){
    #1.获取当前文件夹的目录
    #2.判断要操作安装目录时候有权限操作
    #3.执行操作

    curDir=$(pwd)
    echo ${curDir}
    echo $(_checkPermission /root r w x)
    return 0;
}



function _uninstall_aliasAndEnv(){
    return 0;
}

case $1 in
install)
    echo "开始执行安装alias和环境变量"
    echo "aliasAndEnv安装路径,由bash掉用"$(_install_aliasAndEnv);
    echo "当前执行shell,aliasAndEnv安装路径路径(1.install):$(_getCurrentDir .)"
   ;;
setalias)
        setalias;
         unset setalias;
    ;;
setenv)
        setenv;
         unset setenv;
    ;;
setfunction)
        setfunction;
        unset setfunction;
    ;;
   uninstall)

   ;;
esac
