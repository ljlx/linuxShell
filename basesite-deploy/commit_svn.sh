#!/bin/bash
####################################################
#
# File Name: commit_svn.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年01月11日 星期四 17时37分59秒
###-----------------说明-------------------------###
#                linux 环境 svn提交部署脚本                                  
####################################################
svn update
svn add * --force
commentText="s"
read -p "请输入svn提交备注信息:" commentText
[[ -z $commentText ]] && commentText="."
#echo $commentText
svn commit -m $commentText
