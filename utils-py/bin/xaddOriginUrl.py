#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: addOriginUrl.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-3-12-上午10:24
# ---------------------说明--------------------------
# 当本地ssh-git服务的仓库较多时,不好统一管理.用这个脚本来便于进行仓库的批量操作
# ---------------------------------------------------

import os


def listGitResp(curdir: str = "."):
    tardirlist = os.listdir(curdir)

    def filterGit(item: str):
        return item.endswith(".git")

    return list(filter(lambda item: filterGit(item), tardirlist))


def remoteAddUrl(repoName, remoteUrl):
    gitRespList = listGitResp()

    pass


def tprintList(target: list):
    for item in target:
        print(target)


if __name__ == '__main__':
    tprintList(listGitResp())
