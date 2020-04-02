#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------------------------
# File Name: markdown.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-3-14-下午10:14
#---------------------说明--------------------------
#  markdown 使用.
#---------------------------------------------------

import flask
import markdown
import codecs

app=flask.Flask(__name__)
cssfile='/home/hanxu/document/project/code/personal/develop/studyDoc/src/midware/m2.makedown/md.css'
@app.route("/test1")
def test1():
    in_file="/media/hanxu/d/projectManagement/code/develop/studyDoc/src/midware/m2.makedown/2.table.md"
    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)

    print(html)
    headerDict={}
    headerDict['Content-Encoding']='utf-8'
    headerDict['Content-Language']='zh-cn'
    headerDict['Content-Type']='text/html; charset=utf-8'
    resp=flask.Response(status=200,headers=headerDict)
    resp.response=html
    return resp

def test21():
    md=markdown.Markdown()
    md.convertFile(
        input='/media/hanxu/d/projectManagement/code/develop/studyDoc/src/midware/m2.makedown/2.table.md',
        output='/tmp/test/test.html',encoding='utf-8')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8888)
