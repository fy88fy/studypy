# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 21:29
# @Author  : Feng Xiaoqing
# @FileName: 01.string-study.py
# @Software: PyCharm
# @Function：
#----------------------------------- 


# 练习1：
# 将 “123” 转换成整数
# 将 “9999999999999999999” 转换成长整数
# 将 “3.1415926” 转换成一个浮点数
# 将 123 转换成一个字符串
# 现有以下字符串
# 字符串1："   abc  deFGh&*ijkl opq mnrst((uvwxyz   "
# 字符串2："   ABC#DEF  GH%IJ MNOPQ KLRS&&TUVWX(*&YZ   "
# 使用字符串的各种方法转换成如下方式
# ABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba


a=int("123")
print(type(a))

b=long("9999999999999999999")
print (type(b))


c=float("3.1415926")
print (type(c))


g=123
print (type(g))
h=str(g)
print(type(h))




i="   abc  deFGh&*ijkl opq mnrst((uvwxyz   "
j="   ABC#DEF  GH%IJ MNOPQ KLRS&&TUVWX(*&YZ   "
i=i.strip().upper()
i=filter(str.isalpha, i)
j=j.strip().lower()
j=filter(str.isalpha, j)
l=''.join((i+j).split())
print(i+j[::-1])


