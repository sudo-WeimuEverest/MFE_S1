
from sympy import *
import numpy as np

#牛顿迭代法求解方程
def result(Seniority_Class, average, std):
    for i in range(len(average)):
        a = 1 #迭代初始值
        while a <= 2000 :
            b = a*(1-average[i])/average[i]
            if abs(a*b/(a+b)**2/(a+b+1) - std[i]**2)< 0.000001: #迭代的精度
                print(Seniority_Class[i],':','a=',round(a,4),'b=',round(b,4))
                break
            else:
                x = Symbol("x")
                y=diff(x*x*(1-average[i])/average[i]/(x+x*(1-average[i])/average[i])**2/(x+x*(1-average[i])/average[i]+1) - std[i]**2,x)
                a -= (a*b/(a+b)**2/(a+b+1)-std[i]**2)/y.evalf(subs ={'x':a})

if __name__ == "__main__":
    Seniority_Class = ['Senior_Secured','Senior_Unsecured','Senior_Subordinated','Subordinated','Junior_Subordinated']
    average = [0.5380,0.5113,0.3852,0.3274,0.1709]
    std = [0.2686,0.2545,0.2381,0.2018,0.1090]
    result(Seniority_Class, average, std)
   