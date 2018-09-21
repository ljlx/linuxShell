#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: v1_helloworld.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-21-下午12:56
# ---------------------说明--------------------------
# flask 实例demo
# ---------------------------------------------------
import os

from flask import Flask

curname = __name__
print(curname)
app = Flask(import_name=curname)


@app.route("/os/pwd")
def pwd():
    # return os.execl("ls", "-h", "-l")
    return os.getcwd()


@app.route("/os/ls")
def ls():
    dirlist = os.listdir("/")
    print(dirlist)
    return dirlist


app.run(port=8081, debug=True)

print(pwd())
