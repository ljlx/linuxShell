#!/bin/bash

respName=$1
compName="gfyt"
respRoot="/home/git/"
resp2Root="gfyt/"
if [[ -n ${respName} ]];then
	echo "初始化git仓库: ${respName}"
	#sudo -u git git init --bare ${respName}
	git init --bare ${respName}
	echo "请使用以下:"
	echo "git init"
	echo "git clone git@git.${compName}.lan:${resp2Root}${respName}"
	echo "git remote rename origin old_origin"
	echo "git remote add origin git@git.${compName}.lan:${resp2Root}${respName}"
	
fi


