import math
import numpy as np
import xlrd
from scipy.integrate import tplquad, dblquad, quad

#用于计算Gaussian copula的函数值. 输入x, y以及相关系数p, 得出copula值C(F(x), G(y))
def Gaussian_copula(marginal_x, marginal_y, p):
    Gaussian_copula = []
    for i in range(len(marginal_x)):
        val2 =dblquad(lambda y,x:1/(2*np.pi*math.sqrt(1-p*p))*pow(math.e,-(x*x-2*p*x*y+y*y)/(2*(1-p*p))),float("-inf"),marginal_x[i],float("-inf"),marginal_y[i])
        Gaussian_copula.append(val2)
    return Gaussian_copula

if __name__=="__main__":
    x = np.random.normal(1,2,10)
    y = np.random.normal(2,3,10)
    data = Gaussian_copula(x,y,0.5)
    print(data)
