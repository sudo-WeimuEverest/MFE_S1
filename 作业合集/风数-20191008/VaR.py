import numpy as np
import pandas as pd
from scipy.stats import norm 

class Stock: #定义股票class,调用时可直接返回对应的收益率、方差以及VaR
    #Attention：定义类首字母最好大写
    def __init__(self,price):
        self.price = price
        log_price = np.log(price)
        self.log_return = np.diff(log_price)
    def get_return(self):
        self.returns = np.mean(self.log_return)
        return self.returns
    def get_var(self):
        self.var = np.var(self.log_return)
        return self.var
    def get_VaR(self,a,total,weight): #计算单只股票的VaR
        self.VaR = norm.ppf(a) * np.std(self.log_return)*total*weight 
        return self.VaR

#直接输出每只股票的VaR(by Delta-Normal)
def ind_VaR(P,W): #输入值分别为股票的价格数据和投资权重数据
    columns = P.columns.values.tolist() #获取股票价格数据的列名，即股票的名称
    for name in columns: 
        stock = Stock(P[name])
        weight = W.loc[name,'weight'] #W为储存股票投资权重的矩阵
        ind_VaR = stock.get_VaR(a,total,weight)
        ind_VaR = round(ind_VaR,4) #小数点保留到四位数
        print('%s的VaR为%s' % (name,ind_VaR))

#求股票之间的协方差矩阵后，求出投资组合的VaR
def por_VaR(P,W):
    #求股票收益率的协方差矩阵
    columns = P.columns.values.tolist() #获取股票价格数据的列名，即股票的名称
    R = pd.DataFrame()
    for name in columns: 
        stock = Stock(P[name])
        R[name] = stock.log_return #储存一个对数收益率的dataframe
    Sigma = R.cov()
    Sigma = Sigma.values #求得投资组合的协方差矩阵

    Weight = W.values #将权重向量转化为数组
    W_T = Weight.reshape(1,len(Weight)) #一维向量转置后以备相乘
    W_A = Weight.reshape(len(Weight),1)
    B = np.dot(Sigma, W_A)
    var = np.dot(W_T, B) #计算得到投资组合的方差
    por_VaR = norm.ppf(a) * np.sqrt(var[0][0]) 
    * total#计算投资组合的VaR
    por_VaR = round(por_VaR,4)
    return por_VaR

if __name__=="__main__":
    a = 0.95 #设定计算VaR的置信水平
    total = 1000000 #设定总投资金额
    P = pd.read_excel('C://Users//Lenovo//Desktop//stocks.xlsx',sheet_name=0)#读取股票价格数据
    W = pd.read_excel('C://Users//Lenovo//Desktop//stocks.xlsx',sheet_name=1,index_col='name') #读取股票投资权重数据
    W_weight = W.drop(W.columns[0],1)
    P_price = P.drop('date',1)
    ind_VaR(P_price,W)
    por_VaR = por_VaR(P_price,W_weight)
    print('该投资组合的VaR为%s' % por_VaR)

   
    
    