#!/bin/bash
#--------------------------------------------------
# File Name: ${FILE_NAME}
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-07-03 下午1:34
#---------------------说明--------------------------
#  使用remmina命令来指定配置文件，调用远程桌面。
#---------------------------------------------------


function stop(){
	rdpId=$1
	#入参为空则 kill所有
	if [ -z ${rdpId} ];then
		return $(killAll.sh remmina)
	   else
	    local rdpPid=$(ps aux | grep -v grep | grep ".\.remmina.*${rdpId}" | awk '{print $2}'|xargs);

        if [ ! -z ${rdpPid} ]; then
            local logtxt="PID:[${rdpPid}],rdpId:[${rdpId}]";
            echo "#kill-15 -> ${logtxt}";
            local txt=$(/bin/kill -15 ${rdpPid});
            if [[ $? == 1 ]]; then
            $(/bin/kill -9 ${rdpPid});
            echo "kill-15 has fail ,try used kill-9 ,$?, detail:${logtxt}";
            return $?;
            fi
            echo ${txt};
        fi
	fi

}



function start(){
	
    exec $(nohup remmina -c $@ & 2>&1 > /dev/null);
    return $?;
}

case $1 in
    "id")
    shift;
    #nohup $(start ~/.remmina/1530511931692.remmina);
   ;;
    "name")
    shift;
    rdpName=$1;
    stop ${rdpName};
    nohup $(start ~/.remmina/${rdpName}.remmina);
   ;;

esac
