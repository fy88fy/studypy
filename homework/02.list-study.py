# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 22:27
# @Author  : Feng Xiaoqing
# @FileName: 02.list-study.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
'''

练习2：
现有列表
list1 = ['XXXX', 'b', 3, 'c', '&', 'a', 3, '3', 3, 'aa', '3', 'XXXX']
list2 = ['e', 'f', 'g']
要求对其做以下操作：
1. 取出 ‘XXXX’ 中间的部分，形成一个新的列表list3
2. 对list3 做一下几部操作
1）删除特殊符号
2）统计 3 在list3中出现的次数
3）用最简短的代码去除list3中 26个字母以外的元素(要求只能对list3操作)
4）对list3排序
5）在末尾追加'd',并把list2追加到list3
'''

list1 = ['XXXX', 'b', 3, 'c', '&', 'a', 3, '3', 3, 'aa', '3', 'XXXX']
list2 = ['e', 'f', 'g']

list3=list1[1:-1]
print (list3)
list3.pop(3)
print (list3)

#2
print (list3.count(3))

#3
list3.pop(1)
list3.pop(3)
list3.pop(3)
list3.pop(3)
list3.pop(-1)
print(list3)
#4
list3.sort()
print(list3)

#5
list3.extend("d")
print(list3)
