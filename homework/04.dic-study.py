# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 0:15
# @Author  : Feng Xiaoqing
# @FileName: 04.dic-study.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

'''

练习1：
1. 现有一个字典dict1 保存的是小写字母a-z对应的ASCII码
dict1 = {'a': 97, 'c': 99, 'b': 98, 'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104, 'k': 107, 'j': 106, 'm': 109, 'l': 108, 'o': 96, 'n': 110, 'q': 113, 'p': 112, 's': 115, 'r': 114, 'u': 117, 't': 116, 'w': 119, 'v': 118, 'y': 121, 'x': 120, 'z': 122}

1） 将该字典按照ASCII码的值排序
2） 有一个字母的ASCII错了，修改为正确的值，并重新排序

2. 用最简洁的代码，自己生成一个大写字母 A-Z 及其对应的ASCII码值的字典dict2(使用dict，zip，range方法)

3. 将dict2与第一题排序后的dict1合并成一个dict3

'''

#1
dict1 = {'a': 97, 'c': 99, 'b': 98, 'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104, 'k': 107, 'j': 106, 'm': 109, 'l': 108, 'o': 96, 'n': 110, 'q': 113, 'p': 112, 's': 115, 'r': 114, 'u': 117, 't': 116, 'w': 119, 'v': 118, 'y': 121, 'x': 120, 'z': 122}
print dict(sorted(dict1.iteritems()))

dict1['o']=111
print(dict1)


#2
import string
dict2 = dict(zip(string.uppercase,range(65,92)))
print (dict2)


#4
dict3 = dict(dict1, **dict2)
print dict3



