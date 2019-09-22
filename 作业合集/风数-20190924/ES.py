# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats

#求列表内元素的和
def sum_lists(items):
    sum_lists = 0
    for i in items:
        sum_lists += i
    return sum_lists

#求极限内公式的值
def func(n):
    l = np.random.normal(mu, sigma, size=n) #生成正态分布随机数
    L = sorted(l, reverse=True) #对随机数进行降序排序
    k = int(n*(1-a))
    if k >1: #k大于1时进行求和运算才有意义
        s = sum_lists(L[0:k-1])/k
        return s 
    return 0

#代入参数求解
a =0.99     
mu = 1
sigma =4
ES = []
for n in range (200,int(1e6)):
    f = func(n)
    ES.append(f)
#对于正态分布，ES精确求解公式
es = mu + sigma * stats.norm.pdf(stats.norm.ppf(a))/(1-a)

#画出近似求解到精确结果的收敛图示
plt.plot(ES)
plt.axhline(y = es, color='r',linestyle='-')
plt.savefig(es.jpg)