# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 7:46
# @Author  : Feng Xiaoqing
# @FileName: qiehuanABnginx.py
# @Software: PyCharm
# @Function：
#-----------------------------------

import os
import re
import sys
print'''----------------MENU-----------------
            A.将A组切上去
            B.将A组切下来
            C.将B组切上去
            D.将B组切下来
            E.重启Nginx服务
            F.完成迭代
            G.更新代码
----------------MENU-----------------'''
input=raw_input('Please input your select (Usage:A/B/C/D): ')

#删除配置文件
def RmNginx():
    if os.path.exists('../conf/nginx.conf'):
        os.remove('../conf/nginx.conf')

#下线A组
def OptAdown():
    with open('../conf/nginxmode.conf') as f:
        for line1 in f:
            line1 = line1.replace('server 10.0.0.1:8080', '#server 10.0.0.1:8080')
            line1 = line1.replace('server 10.0.0.2:8080', '#server 10.0.0.2:8080')
            with open('../conf/nginx.conf', 'a') as f1:
                f1.write(line1)

#上线A组
def OpeAup():
    with open('../conf/nginxmode.conf') as f:
        for line1 in f:
            line1 = line1.replace('#server 10.0.0.1:8080', 'server 10.0.0.1:8080')
            line1 = line1.replace('#server 10.0.0.2:8080', 'server 10.0.0.2:8080')
            with open('../conf/nginx.conf', 'a') as f1:
                f1.write(line1)

#下线组
def OpeBdown():
    with open('../conf/nginxmode.conf') as f:
        for line1 in f:
            line1 = line1.replace('server 192.168.0.1:8080 weight=100', '#server 192.168.0.1:8080 weight=100')
            line1 = line1.replace('server 192.168.0.2:8080 weight=100', '#server 192.168.0.2:8080 weight=100')
            with open('../conf/nginx.conf', 'a') as f1:
                f1.write(line1)


#上线B组
def OpeBup():
    with open('../conf/nginxmode.conf') as f:
        for line1 in f:
            line1 = line1.replace('#server 192.168.0.1:8080 weight=100', 'server 192.168.0.1:8080 weight=100')
            line1 = line1.replace('#server 192.168.0.2:8080 weight=100', 'server 192.168.0.2:8080 weight=100')
            with open('../conf/nginx.conf', 'a') as f1:
                f1.write(line1)

def main():
    if input == 'A':
        print "You select is A,Now down A Server."
        RmNginx()
        OptAdown()

    if input == 'B':
        print "You select is A,Now down A Server."
        RmNginx()
        OpeAup()

    if input == 'C':
        print "You select is ,Now down  Server."
        RmNginx()
        OpeBdown()

    if input == 'D':
        print "You select is ,Now down  Server."
        RmNginx()
        OpeBup()

    if input == 'E':
        print "/usr/sbin/nginx -s reload  finished.Nginx启动完成"

    if input == 'F':
        print "完成迭代"

    if input == 'G':
        print "代码已更新完成"

if __name__ == '__main__':
    main()