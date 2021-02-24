# @Time : 2021/2/21 15:22
# @Author : Yuqiao Gai
# @File : demo7.py
# @Software: PyCharm
# coding:utf-8
'''商场打折'''
answer=input("您是会员吗？y/n");
money= float(input("您的消费金额："));
if answer=='y':
    print("消费金额为",money*0.8);
else :
    print("消费金额为",money);


