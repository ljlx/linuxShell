#!/bin/bash
####################################################
#
# File Name: maven.env.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年01月31日 星期三 14时36分04秒
###-----------------说明-------------------------###
#                                                   
####################################################
defaultHome='/usr/share/maven';
defaultRepo='/usr/share/maven-repo';
myMvnHome='~/.m2/mavenBin';
myMvnRepo='~/.m2/repository';
userHome=$(_getHomePath);
m2Home=${userHome}'.m2';

if [[ ! -d ${m2Home} ]]; then
#    dirname ${m2Home};
    mkdir ${m2Home};
fi

if [[ -d ${defaultpkg} && ! -d ${myMvnHome} ]]; then
    ln -s ${defaultpkg} ${myMvnHome};
fi

if [[ -d ${defaultRepo} && ! -d ${myMvnRepo} ]]; then
    ln -s ${defaultRepo} ${myMvnRepo};
fi

export M2_HOME=~/.m2/mavenBin;
export M2_RESP=~/.m2/repository
export PATH=$PATH:$M2_HOME/bin
echo "maven env set finish"
