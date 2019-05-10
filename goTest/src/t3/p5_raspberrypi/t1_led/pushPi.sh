#!/usr/bin/env bash
#--------------------------------------------------
# File Name: pushPi.sh
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-5-10-上午11:21
#---------------------说明--------------------------
# 编译并push到pi中
#---------------------------------------------------

exename="gotestLed"

CGO_ENABLED=0 GOOS=linux GOARCH=arm go build -o ${exename} ./MainLed.go && rsync ${exename} pi.gfyt.wan:gobin/

md5sum ${exename}

#ssh pi.gfyt.wan