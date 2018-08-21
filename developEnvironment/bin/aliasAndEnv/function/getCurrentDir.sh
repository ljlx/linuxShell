#!/bin/bash
####################################################
#
# File Name: getCurrentDir.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年03月03日 星期六 16时27分42秒
###-----------------说明-------------------------###
#获取当前执行的shell文件的实际路径
####################################################
function _getCurrentDir(){
    dir=$1;
    if [ -z ${dir} ]; then
        dir=${BASH_SOURCE[0]}
    fi
    echo "获取当前路径的来源getCurrentDir: $(set | grep BASH_SOURCE)"
    curdir=$(cd $(dirname ${dir}); pwd )
    echo "getCurrentDir:"${curdir}
};