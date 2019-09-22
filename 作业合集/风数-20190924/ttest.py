# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:48:22 2019

@author: Lenovo
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

if __name__ == '__main__':
    with open(r'C:\Users\Lenovo\Desktop\tRandom.txt','r') as f: #读取储存的数据
        data =[]
        for line in f:
            data.append(float(line.strip()))  
        n = 20#此处自由度应与生成随机数时所指定的相同
        c = 'df = '+ str(n)
        x = np.linspace(-4,4,50) 
        plt.plot(x, t.pdf(x,n), label=c,color ='r') #绘制t分布的图像
        #plt.plot(x,norm.pdf(x,0,1), color='yellow')
        #绘制随机数的频率直方图，以进行比较
        plt.hist(data,bins=50,density = True)
        plt.legend()
        plt.savefig('trandom.jpg')
    exit(0)