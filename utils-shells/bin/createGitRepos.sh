#!/bin/bash
#--------------------------------------------------
# File Name: createGitRepos.sh
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-06-14 下午5:02
###-----------------说明-------------------------###
# 创建git仓库
####################################################
repoName=$1
currpath=$pwd
svnUser=svnserve
repoPath=/root/allServer/svnServer/SVNServerRepository/
configPath=/root/allServer/svnServer/config
#svnConfPath=ln -s ../../config/ conf
#测试svn仓库目录是否已存在该目录
cd $repoPath
svnadmin create $repoName
cd $repoName
#如果上个操作为true
#if [ ];
rm -r ./conf
ln -s ${configPath} conf
cd ../
chown -R $svnUser:$svnUser ./$repoName
cd $currpath
echo "创建仓库[ " $repoName " ]完成"

#fi

#查询大文件的top10 列表
#git verify-pack -v .git/objects/pack/pack-252132d8532c30efffcb83d335cc11ce825debb4.idx | sort -k 3 -n | tail -10 | awk '{print $1}'

#在找出指定的文件，对应的这些文件路径
#git rev-list --objects --all | grep -E "b185971b|fa1d66a0|ad6b2e42|3033db9c|d362e08c|101ac98f|79371045|293be777|e560875e|4f33d2d2"
