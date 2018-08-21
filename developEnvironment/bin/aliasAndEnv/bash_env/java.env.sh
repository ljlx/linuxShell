#!/bin/bash
####################################################
#
# File Name: java.env.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年01月31日 星期三 14时33分31秒
###-----------------说明-------------------------###
#                                                   
####################################################
jdkhome=/usr/lib/jvm/java-openjdk-enable

if [ ! -d $jdkhome ];then
        echo "warn>>>> jdk is not set links /usr/lib/jvm/java-openjdk-enable "
fi

#用作idea的jdk使用路径
# ---------------------------------------------------------------------
# Locate a JDK installation directory which will be used to run the IDE.
# Try (in order): IDEA_JDK, idea.jdk, ./jre64, JDK_HOME, JAVA_HOME, "java" in PATH.
# ---------------------------------------------------------------------

export IDEA_JDK=/usr/lib/jvm/ideajdk


export JAVA_HOME=/usr/lib/jvm/java-openjdk-enable

export IDEA_JDK_64=
#$JAVA_HOME
export CLASSPATH=.:$JAVA_HOME/lib/rt.jar
export PATH=$PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin

export | grep JAVA_HOME
