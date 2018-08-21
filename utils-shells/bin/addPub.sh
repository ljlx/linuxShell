#!/bin/bash
####################################################
#
# File Name: addPub.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年01月30日 星期二 12时49分42秒
###-----------------说明-------------------------###
#  将公钥文件夹下的公钥生成进auth*文件中
####################################################
source ${PUB_FACTION}/getHomePath.sh
svnPath=svn://mysvn.thesunboy.com:8443/releaseServer/shellScript/trunk/developEnvironment/bin/aliasAndEnv/mySshPubs/pubs
pubsDir=$(_getHomePath)/.ssh/pubs/
authFile=$(_getHomePath)/.ssh/authorized_keys
authBackDir=$(_getHomePath)/.ssh/backAuth/


if [ ! -d ${authBackDir} ];then
    mkdir ${authBackDir}
fi
if [ ! -d ${pubsDir} ];then
    mkdir ${pubsDir}
    if [ ! -z $(which svn) ]; then
        $(which svn) checkout ${svnPath} ${pubsDir} ;
    fi
fi

#关于字符串截取的说明：
#  ‘#*/’号从左边开始计算，删除第一个 /号左边字符，保留右边字符
#  ‘##*/’号从右边开始计算，删除第一个 /号左边字符，保留右边字符
#  ‘%/*’号表示从右边开始，删除第一个 /号及右边的字符，保留左边字符就就阿斯顿阿斯顿上的阿斯顿
#  '%%/*'号表示从左边开始，ggg绝好机会删除第一个 /号及右边的字符，保留左边字符jjj就j就事实上身上身上事实上

if [ -f ${authFile} ];then
    curdate=$(date "+%y-%m-%d-%H%M%S")
    fileName=${authFile##*/};
    mv ${authFile} ${authBackDir}"${fileName}"-${curdate}.bak
fi

touch ${authFile}
    index=1
    for item in `find ${pubsDir} -type f -name "*.pub"`
     do
        echo  "applying auth file $item"
        pubname=${item##*/};
        echo -e "## $index. $pubname start..." >> ${authFile}
        cat ${item} >> ${authFile}
        echo -e "## $index. $pubname end <--\n" >> ${authFile}

       let index++ 
        done

#生成
function genkey(){

    return 0;
}
