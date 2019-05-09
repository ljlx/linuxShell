#!/bin/bash
####################################################
#
# File Name: network.alias.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年01月31日 星期三 13时32分25秒
###-----------------说明-------------------------###
#                                                   
####################################################

alias nmap='nmap -A -T4'
#alias ssh='ssh -p 1113 -i ~/.ssh/localhost.pri '
#alias scp='scp -P 1113 -i ~/.ssh/localhost.pri '
alias assh='ssh -i ~/.ssh/localhost.pri '
alias ascp='scp -i ~/.ssh/localhost.pri '
#a归档模式,v-verbose详细输出,h-human-readable
alias rsync='rsync -avh --rsh=ssh'