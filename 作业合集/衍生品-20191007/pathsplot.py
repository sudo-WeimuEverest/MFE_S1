# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:48:22 2019

@author: Lenovo
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

if __name__ == '__main__':
    for i in range(1,101): #此处range右限需对应改为NumberOfPaths+1
        #filename = C:/Users/Lenovo/Desktop//price/.txt
        with open('C:/Users/Lenovo/Desktop/price/'+str(i)+'.txt','r') as f: #读取储存的数据
            data =[]
            for line in f:
                data.append(float(line.strip()))  
        plt.yticks([])
        plt.plot(data) #分别将路径绘制到图中
    plt.savefig('C:/Users/Lenovo/Desktop/stock.jpg')
    exit(0)