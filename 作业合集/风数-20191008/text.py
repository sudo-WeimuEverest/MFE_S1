import numpy as np
import pandas as pd
from scipy.stats import norm 


#if __name__=="__main__":
#    a = 0.95 #设定计算VaR的置信水平
#    total = 1000000 #设定总投资金额
#    P = pd.read_excel('C://Users//Lenovo//Desktop//stocks.xlsx',sheet_name=0) #读取股票价格数据
W = pd.read_excel('C://Users//Lenovo//Desktop//stocks.xlsx',sheet_name=1,index_col='name') #读取股票投资权重数据
#ind_VaR(P,W)

def test(pd):
    pd = pd.DataFrame()
    columns = W.columns.values.tolist()
    for i in columns:
        print(W[i])

if __name__=='__main__':
    test(W)

