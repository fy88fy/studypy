# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 22:46
# @Author  : Feng Xiaoqing
# @FileName: 03.Variable-study.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
'''
Variable变量
练习3. 现有两个变量
a = ('h',)
b = ('h')
1）将a和b分别追加到上一题的list3中，观察有什么区别
2）将1生成的list3转换成元组(扩展：自己搜索方法)
3）打印出只有一个元素'h'的元组，在2中生成的元组中的索引
'''

list3=['a', 'aa', 'b', 'c', 'd', 'e', 'f', 'g']
a = ('h',)
b = ('h')

list3.append(a)
print (list3)

list3.append(b)
print(list3)

#2
t=tuple(list3)
print (t)

#3
print(t[-2])
print(t.index(t[-2]))



