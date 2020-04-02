#!/bin/bash
####################################################
#
# File Name: checkPermission.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年02月04日 星期日 23时10分42秒
###-----------------说明-------------------------###
#检查指定的目录or文件是否具有指定的r w x 等 权限,具有操作权限则返回0,否咋返回1
#参数:$1[operDir]{/etc/sysconfig}  $234...[needcheckPermission]{r w x f d L}
#结果:$? exitCode
####################################################

function _checkPermission(){
operDir=$1 && shift && operPermission=$@
   #d:目录 f:文件 r:可读 w:可写 x:可执行 可能有多个
    for var in ${operPermission[@]}
        do
            #以此判断这个目录or文件是否具有这个权限,有一个不满足这直接return false
            #x$1 != x  其中x只是一个胎记
              if [[ ${var} = "r" && ! -r ${operDir} ]]; then
               echo "r-access deind;"
                return 1;
              elif [[ ${var} = 'w' && ! -w ${operDir} ]];then
                echo "w-access deind;"
                return 2;
              elif [[ ${var} = "x" && ! -x ${operDir} ]];then
             echo "x-access deind;"
                return 3;
              elif [[ ${var} = "d" && ! -d ${operDir} ]];then
              echo "d-access deind;"
                return 4;
              elif [[ ${var} = "f" && ! -f ${operDir} ]];then
              echo "f-access deind;"
                return 5;
               elif [[ ${var} = "L" && ! -L ${operDir} ]];then
              echo "L-access deind;"
                return 6;
            fi
        done
 }