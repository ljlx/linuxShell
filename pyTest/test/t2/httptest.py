#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------------------------
# File Name: httptest.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-2-16-下午8:07
#---------------------说明--------------------------
# simplehttpServertest
#---------------------------------------------------

from socketserver import TCPServer

def reqHandler():
    pass

def start():
    myserver=TCPServer(server_address=("0.0.0.0",1111),RequestHandlerClass=reqHandler)
    req=myserver.get_request()
    print(req)

if __name__ == '__main__':
    import argparse
    mainarg=argparse.ArgumentParser(add_help="开启简单的tcp-server.")
    mainarg.add_argument("-v","--verbosity",action="count",default=0,help="统计参数出现的次数.")
    mainarg.add_argument("-t1","--test-1",help="测试choice参数",choices=['1','2','3'])
    mainarg.parse_args()
    # mainarg.add_argument("start",action=)
    # start()