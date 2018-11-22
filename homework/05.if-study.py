# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 0:27
# @Author  : Feng Xiaoqing
# @FileName: 05.if-study.py
# @Software: PyCharm
# @Function：
#-----------------------------------
'''
练习2
1. 输入三个整数x,y,z，请把这三个数由小到大输出。   1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，   然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。



'''
#1
a = raw_input("Please input a num a: ")
b = raw_input("Please input a num b: ")
c = raw_input("Please input a num c: ")
int(a)
int(b)
int(c)

if a > b:
    x = a
    if b > c:
        y = b
        z = c
        print "%s > %s > %s" % (x,y,z)
    elif b < c:
        y = c
        z = b
        print"%s > %s > %s" %  (x,y,z)
    else:
        print"%s > %s = %s"  % (x,y,z)
if a < b:
    x = b
    if a > c:
        y = a
        z = c
        print"%s > %s > %s" % (x, y, z)
    elif a < c:
        y = c
        z = b
        print" %s > %s > %s" % (x, y, z)
    else:
        print"%s > %s = %s" % (x, y, z)
if a == b:
    x = a
    if b > c:
        y = b
        z = c
        print"%s = %s > %s" % (x, y, z)
    elif b < c:
        y = b
        z = c
        print"%s = %s < %s"% (x, y, z)
    else:
        print"%s = %s = %s" % (x, y, z)



'''
2. 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高   于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提   成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于   40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于   100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''

