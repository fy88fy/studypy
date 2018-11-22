# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 21:54
# @Author  : Feng Xiaoqing
# @FileName: 06.for-study.py
# @Software: PyCharm
# @Function：
#-----------------------------------
'''
练习1
1. 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？ 1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
2. 打印出所有的“水仙花数”,所谓“水仙花数”是指一个三位数,其各位数字立方和等于该数本身。例如：153是一个“水仙花数”,因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数,每个数分解出个位,十位,百位。
3. 两个乒乓球队进行比赛,各出三人。甲队为a,b,c三人,乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比,c说他不和x,z比,请编程序找出三队赛手的名单。
'''
#----------------------------------------------
#1
sum=0
list1=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            d = a*100 + b* 10 +c
            if a != b and a != c and b != c:
                sum+=1
                print (d)
                list1.append(d)
print "Totol is %s" % sum
print(list1)





'''
结果：
Totol is 24
[123, 124, 132, 134, 142, 143, 213, 214, 231, 234, 241, 243, 312, 314, 321, 324, 341, 342, 412, 413, 421, 423, 431, 432]

'''
#方法二

i=0

num=(1,2,3,4)
for x in  num:

       for y in num:

           for z in num:

               if x != y and  x != z and  y != z :

                    print x*100+y*10+z

                    i=i+1

print "the total num is :%s" % i


#------------------------------------------------------------------
#2

for a in range(1,9):
    for b in range(0,9):
        for c in range(0,9):
            if a*100+b*10+c == a**3+b**3+c**3:
                print"%s%s%s" % (a,b,c)

'''
结果：
153
370
371
407
'''
#--------------------------------------------------------------------

#3.
list1=['a','b','c']
list2=[]

for i in ('a','b' ,'c'):
    for j in ('x','y','z'):
        if not (i == 'a' and j == 'x'):
            if not (i == 'c'and j == 'x'):
                if not (i == 'c' and j == 'z'):
                     print "%s--%s" %(i,j)
'''
结果：
a--y
a--z
b--x
b--y
b--z
c--y

'''