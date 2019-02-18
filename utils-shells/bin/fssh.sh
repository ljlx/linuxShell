#!/bin/bash
####################################################
#
# File Name: fssh.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年09月06日 星期三 22时00分58秒
###-----------------说明-------------------------###
#  快速进入我常用的 ssh服务器中
####################################################
source ${PUB_SHELLS}/developEnvironment/bin/aliasAndEnv/function/getHomePath.sh
authDir=$(_getHomePath)
authFile=${authDir}/.ssh/localhost.pri

#[-eq 用于数字 不能用于字符串 ,最好使用=比较],判断为空时,需要变量加上引号 非空判断: ! -z 或者 -n
server=$1;
#nas,mint,deepin,aliyun,hkyun


function sshRemote(){
    echo "try connecting [${2}]";
    echo $@;
#    TODO 将来在使用python改写这个脚本的时候,需要考虑,如果config文件配置了密钥,就不再带-i参数
#    $(which ssh) -i ${authFile} $@
    $(which ssh) $@
}


case ${server} in
    mint)
        sshRemote hanxu@vpn.home
        ;;
    nas)
        sshRemote root@10.193.1.2
        ;;
    bj)
        sshRemote root@vpn.vpn
        ;;
    vpnhk)
        sshRemote root@vpn.hk
        ;;
    hk)
        sshRemote root@hk.thesunboy.com
	;;
    nasloop)
        sshRemote root@10.192.1.1
        ;;
    comp)
        sshRemote hanxu@vpn.company
	    ;;
    t1)
	shift;
	user=${@};
	if [[ -z ${user} ]];then
		user=$(whoami);
	fi
	sshRemote ${user}@t1.company.wan
	    ;;
   t2)
	echo "pkvOPfezonOiUT4W"
	sshRemote hanxu@jumps.linkdood.cn

	;;
     oth*)
	    shift;
	    sshRemote $@
	    ;;
    *)
        echo "fssh.sh ( mint| nas| bj |hk |nasloop |comp |wbt1),
            oth* root@test.com
        "

        ;;
esac

