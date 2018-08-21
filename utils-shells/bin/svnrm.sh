#!/bin/bash
####################################################
#
# File Name: svnrm.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2017年11月04日 星期六 15时43分37秒
###-----------------说明-------------------------###
#                                                   
####################################################
#svn st | awk '{if ($1 == "!") {print $2}}' | xargs svn rm


resu=$(find ./ -name $1)
for item in ${resu}
do
	echo ${item}
	svn del ${item}
done
