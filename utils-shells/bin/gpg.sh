#!/usr/bin/env bash
#--------------------------------------------------
# File Name: gpg.sh
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-3-26-下午10:04
#---------------------说明--------------------------
# gpg相关操作
#---------------------------------------------------


case $1 in
"tty")
    export GPG_TTY=$(tty)
    env|grep GPG
   ;;
esac