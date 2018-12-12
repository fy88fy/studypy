# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 7:39
# @Author  : Feng Xiaoqing
# @FileName: login.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
import os
import re
# import settings
# settings.userinfo()
# # print(user1)
class login(object):

    user = raw_input('请输入用户名： ')
    password = raw_input('请输入密码： ')
    loginfo = '../log/loginfo'

    def login(self):

        with open('../conf/userinfo') as f:
             for userinfo in f.readlines():
                userinfo = userinfo.strip().split(':')
                if self.user in userinfo:
                    if self.user == userinfo[0]:
                        if self.password  == userinfo[1]:
                            print ("登录成功")
                            with open('../log/loginfo', "r") as f1:
                                for line in f1:
                                    name = line.strip().split(':')
                                    if self.user != name[0]:
                                        with open("%s.bak" % self.loginfo, "a") as f2:
                                            f2.write(line)
                                    else:
                                        if self.user == name[0]:
                                            line1 = line.strip().split(':')
                                            line2=int(line1[1])+1
                                            print"这是%s第%s次登录系统" % (self.user,line2)
                                            with open("%s.bak" % self.loginfo, "a") as f2:
                                                f2.write(re.sub(line1[1],str(line2), line))
                            os.remove(self.loginfo)
                            os.rename("%s.bak" % self.loginfo, self.loginfo)
                        else:
                             print ("用户名或密码错误，请重试")

Login = login()
while Login.login():
    Login.login()



