# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 7:39
# @Author  : Feng Xiaoqing
# @FileName: login.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
import os,re
user=raw_input('请输入用户名： ')
password=raw_input('请输入密码： ')
loginfo='../log/loginfo'
def login():
    with open('../conf/userinfo') as f:
         for userinfo in f.readlines():
            userinfo = userinfo.strip().split(':')
            if user in userinfo:
                if user == userinfo[0]:
                    if password  == userinfo[1]:
                        print ("登录成功")
                        with open('../log/loginfo', "r") as f1:
                            for line in f1:
                                name = line.strip().split(':')
                                if user != name[0]:
                                    with open("%s.bak" % loginfo, "a") as f2:
                                        f2.write(line)
                                else:
                                    if user == name[0]:
                                        line1 = line.strip().split(':')
                                        line2=int(line1[1])+1
                                        print"这是%s第%s次登录系统" % (user,line2)
                                        with open("%s.bak" % loginfo, "a") as f2:
                                            f2.write(re.sub(line1[1],str(line2), line))
                        os.remove(loginfo)
                        os.rename("%s.bak" % loginfo, loginfo)
                    else:
                        print ("用户名或密码错误，请重试")
         else:
             exit
login()
