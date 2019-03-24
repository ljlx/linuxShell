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


targetList=(~/.GO/thirdPkg \
~/.GO/target \
/usr/lib/go \
)

targetPath="/tmp/target"
for item in ${targetList[@]} ; do
    targetPath=${targetPath}:${item}
done

#该环境变量,如果在有多个值时,在使用go get [位置信息] 命令时,下载的包会默认存在第一个目录.
#e.g: go get github.com/hx940929/linuxShell/goTest/
export GOPATH=${targetPath}
