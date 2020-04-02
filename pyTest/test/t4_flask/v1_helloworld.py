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
from flask import request
from flask import Response

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
    respstr = '\r\n'.join(dirlist)
    return respstr


@app.route("/curl")
def testcurl():
    requ = Flask.before_request

    print("reqest:", request.path)

    body = str(request.input_stream)
    print(body)
    reqheader = request.headers

    strbuild = ""
    for item in reqheader.items():
        print("requestHead:", item)
        strbuild += str(item)
    strbuild += "\n"
    # respdata=strbuild.join(reqheader.items())
    headerDict = {}
    headerDict['Content-Encoding'] = 'utf-8'
    headerDict['Content-Language'] = 'zh-cn'
    headerDict['Content-Type'] = 'text/plain; charset=utf-8'
    resp = Response(status=200, headers=headerDict)

    # resp.set_data(strbuild)
    resp.response = strbuild

    return resp


if __name__ == '__main__':
    app.run(port=8088, debug=True)
    print(pwd())
