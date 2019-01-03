#!/bin/bash
#--------------------------------------------------
# File Name: frp.sh
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-3-上午9:14
#---------------------说明--------------------------
# 使用此脚本安装,启动frp程序. 以及安装service启动文件.
#---------------------------------------------------
PRG="$0"

while [ -h "$PRG" ]; do
  ls=`ls -ld "$PRG"`
  link=`expr "$ls" : '.*-> \(.*\)$'`
  if expr "$link" : '/.*' > /dev/null; then
    PRG="$link"
  else
    PRG=`dirname "$PRG"`/"$link"
  fi
done
echo "test==> $PRG"