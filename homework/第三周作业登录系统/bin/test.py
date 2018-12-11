# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 8:30
# @Author  : Feng Xiaoqing
# @FileName: test.py
# @Software: PyCharm
# @Function：
#-----------------------------------

user=raw_input('请输入用户名： ')
password=raw_input('请输入密码： ')

with open('../log/login', "r", encoding="utf-8") as f1:
    for line in f1:
        with open("%s.bak" % loginfo, "w", encoding="utf-8") as f2:
        f2.write(re.sub('1', '2', line))
    os.remove(loginfo)

    os.rename("%s.bak" % loginfo, loginfo)