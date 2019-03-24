#!/usr/bin/env bash
#--------------------------------------------------
# File Name: go.env.sh
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-3-24-下午3:29
#---------------------说明--------------------------
# go 语言环境变量设置.
#---------------------------------------------------

GOHOME=/usr/lib/go

GOROOT=${GOHOME}/bin

export GOHOME=${GOHOME}
export GOROOT=${GOROOT}

export PATH=${PATH}:${GOROOT}


targetList=(/tmp/target \
~/.Go_target \
)

targetPath="/tmp/target"
for item in ${targetList[@]} ; do
    targetPath=${targetPath}:${item}
done

export GOPATH=${targetPath}
