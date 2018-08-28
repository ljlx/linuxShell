#!/usr/bin/python3
#coding=utf-8
#--------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-06-25 下午1:52
#---------------------说明--------------------------
#  
#---------------------------------------------------

# 我是开发分支，
# 开发呀。
# 开发呀。
# 开发呀。
#
# 再次开发呀，开发呀，不能提交喔40%
# 再次开发呀，开发呀，不能提交喔50%
# 呀，突然给我个bug了， 又不能提交，/wn ，那就只能先暂存一下那。git stash,保存当前进度，然后在master上开一个新的issue分支
#     git stash
#     git checkout master
#     git checkout -b issue-2
#         修复bug， bug是os.py 文件第10行的，多了最后一个字母a
# bug,修复完毕。
#          git commit -a -m "修复原因"     at branch of issue-2
#     git checkout master
#         合并issue分支到master， git merge --no-ff issue-2
#         删除issue分支  git branch -d issue-2
#  切换回原来的dev分支
#    恢复暂存  git stash pop
# 继续开发分支60%。
# 开发呀
# 开发呀
# 开发完毕100%
# 准备提交
# git commit -a -m "分支开发完毕"
#推送分支到远程仓库 git push origin devTest3
# 来自其他小伙伴的分支推送..


