# @Time : 2021/1/30 21:59
# @Author : Yuqiao Gai
# @File : demo6.py
# @Software: PyCharm
# coding:utf-8
score= int(input ('请输入一个成绩：'))
if 90<=score<=100 :
    print('A')
elif score<90 and score>=80:
    print('B')
elif score<80 and score>=70:
    print('C')
else :
    print('D')
