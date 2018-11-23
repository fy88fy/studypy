# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 21:55
# @Author  : Feng Xiaoqing
# @FileName: 07.while-study.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
'''
练习2
1. 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：对n进行分解质因数,应先找到一个最小的质数i,然后按下述步骤完成：
(1)如果分解后商为1,则说明分解质因数的过程已经结束,打印出即可。
(2)如果商不为1,则应打印出i的值,并用n除以i的商,作为新的正整数进行分解,
　重复执行第一步。
(3)如果n不能被i整除,则i的值加1,重复执行第一步。
2. 猴子吃桃问题：猴子第一天摘下若干个桃子,当即吃了一半,还不瘾,又多吃了一个，第二天早上又将剩下的桃子吃掉一半,又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时,见只剩下一个桃子了。求第一天共摘了多少。
程序分析：采取逆向思维的方法,从后往前推断。
'''

#1
for num in range(100):
    # num = raw_input("please in put a number: ")
    num=int(num)
    if num <= 1:
        pass
        #print('这不是质数')
    elif num == 2:
        pass
        #print('这是一个质数!')
    else:
        i=2
        while i < num:
            if num%i == 0:
                pass
                #print('这不是一个质数')
                break
            i += 1
        else:
            print num,('这是一个质数!')


#
i=0
while n != 1:
    n=n/2-1

    i+=1
    if i==10:
        break
        print n





