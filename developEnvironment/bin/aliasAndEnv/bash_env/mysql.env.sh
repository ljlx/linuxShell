#!bin/bash
####################################################
#
# File Name: mysql.env.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年05月02日 星期三 14时04分04秒
###-----------------说明-------------------------###
#
####################################################
mysql_HOME=/data/mysql_sandbox/package/5.7.21

export MYSQL_HOME=${mysql_HOME}
export PATH=$PATH:${MYSQL_HOME}/bin