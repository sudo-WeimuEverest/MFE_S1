import numpy as np
import pandas as pd 

#使用EVT估计VaR
def EVT_VaR(r,a): #输入值为对数收益率以及置信水平
    n = r.shape[0]
    Nu = 50 #阅读相关文献，取u使得超过阀值数目为50
    r = r.r.sort_values() #降序排列
    u = r[Nu] 
    e = 1/50*np.log(r[:Nu]/u).sum() #该部分为形状参数的MLE
    c = Nu /n *abs(u)**(1/e) #为尺度参数和形状参数估计值的比值
    VaR = u + c*((n/Nu*(1-a)**(-e))-1)
    return VaR
#根据VaR求ES
def ES(r,VaR):
    a = []
    for i in r.r:
        if i > VaR:
            a.append(i)
    ES = sum(a)/len(a)
    return ES
    
if __name__ == '__main__':
    a = 0.95
    r = pd.read_excel('C://Users//Lenovo//Desktop//50ETF.xlsx')
    VaR = EVT_VaR(r,a)
    ES = ES(r, VaR)
    print(VaR)
    print(ES)