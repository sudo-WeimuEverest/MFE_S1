# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats
from numba import autojit
import time

start =time.time()

@autojit
def func(a,mu,sigma,n):
    l = np.random.normal(mu, sigma, size=n) #生成正态分布随机数
    l.sort() #对随机数进行降序排序
    k = int(n*a)
    s = l[k:].mean()
    return s

@autojit
def main(lists):
    for n in range (200,10000):
        f = func(a,mu,sigma,n)
        lists.append(f)
    es = mu + sigma * stats.norm.pdf(stats.norm.ppf(a))/(1-a)
    plt.axhline(y = es, color='r',linestyle='-')
    plt.plot(ES)
    plt.savefig('es.jpg')

ES = []
if __name__ == '__main__':
    a =0.99     
    mu = 1
    sigma =4
    main(ES)

end = time.time()
print('Running time: %s Seconds'%(end-start))