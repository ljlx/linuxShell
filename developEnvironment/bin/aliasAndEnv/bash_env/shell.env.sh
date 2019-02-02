#!/bin/bash
####################################################
#
# File Name: shell.env.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年01月31日 星期三 14时36分42秒
###-----------------说明-------------------------###
#
####################################################
export PUB_SHELLS=/usr/linuxShell/

shellUtilPath=${PUB_SHELLS}/utils-shells/bin
pyUtilpath=${PUB_SHELLS}/utils-py/bin


mpath=${PUB_SHELLS}/utils-shells/bin:$PATH
mpath=${pyUtilpath}:$PATH

export PATH=${mpath}



export PUB_FACTION=${PUB_SHELLS}/developEnvironment/bin/aliasAndEnv/function


