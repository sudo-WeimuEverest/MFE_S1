import pandas as pd 
import numpy as np 

def get_rating(value,firm= 'firm1'):
    """
    :value: 输入生成的收益值
    :param firm:对应不同的公司，不同公司对应的阀值范围不同
    :return： 返回收益值对应的评级
    """
    # 对应每家公司的阀值
    if firm != 'firm1':
        if firm == 'firm2':
            z = [3.12,1.98,-1.51,-2.30,-2.72,-3.19,-3.24]
        else:
            z = [2.86,2.72,2.63,2.11,1.74,1.02,-0.85] #更改原表中ZA为2.72
    else:
        z = [3.54,2.78,1.53,-1.49,-2.18,-2.75,-2.91]
    #将收益与阀值对应
    if value >= z[0]:
        return 'AAA'
    elif value >= z[1]:
        return 'AA'
    elif value >= z[2]:
        return 'A'
    elif value >= z[3]:
        return 'BBB'
    elif value >= z[4]:
        return 'BB'
    elif value >= z[5]:
        return 'B'
    elif value >= z[6]:
        return 'CCC'
    else:
        return 'Def'

#根据评级计算组合的价值
def por_value(r1,r2,r3):
    #三项资产不同评级对应的价值
    v1 = {'AAA':4.375,'AA':4.368,'A':4.346,'BBB':4.302,'BB':4.081,'B':3.924,'CCC':3.346,'Def':2.125}
    v2 = {'AAA':2.132,'AA':2.130,'A':2.126,'BBB':2.113,'BB':2.063,'B':2.028,'CCC':1.774,'Def':1.023}
    v3 = {'AAA':1.162,'AA':1.161,'A':1.161,'BBB':1.157,'BB':1.142,'B':1.137,'CCC':1.056,'Def':0.551}
    total = v1[r1]+v2[r2]+v3[r3]
    return total
#由指定的相关系数矩阵计算组合价值,n为monte calro模拟的次数
def value(n):
    #基于相关系数矩阵生成收益的随机数
    mean = (0,0,0)
    cov = [[1.0,0.3,0.1],[0.3,1.0,0.2],[0.1,0.2,1.0]]
    R = np.random.multivariate_normal(mean,cov, n) #年末随机收益矩阵，每一行对应三项资产的收益
    intial_value = [4,2,1] #三项资产的初始价值
    value = []
    for i in range(0,n-1):
        v1 = intial_value[0]+ R[i,0]
        v2 = intial_value[1]+ R[i,1]
        v3 = intial_value[2]+ R[i,2]
        r1 = get_rating(v1,firm='firm1')
        r2 = get_rating(v2,firm='firm2')
        r3 = get_rating(v3,firm='firm3')
        result = por_value(r1,r2,r3)
        value.append(result)
    return value

if __name__ == '__main__':
   #生成3000个模拟结果
   MC = value(3000)
   #计算组合价值得统计指标
   mean = np.mean(MC).round(3)#均值
   median = np.median(MC).round(4)#中位数
   tile95 = np.percentile(MC,95).round(4)#95%分位数
   tile5 = np.percentile(MC,5).round(4)#5%分位数
   print(mean,median,tile95,tile5)
    
   
    

