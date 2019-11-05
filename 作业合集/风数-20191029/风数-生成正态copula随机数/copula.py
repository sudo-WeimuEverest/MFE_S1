import numpy as np 
import pandas as pd
from scipy import optimize
from scipy import stats
from numpy import random 
import math

class Copula():
    def __init__(self,data):
        self.cov = np.cov(data[0].T) #输入数据的cov
        self.data = np.array(data)
        self.normal = stats.multivariate_normal([0 for i in range(len(data[0]))], self.cov,allow_singular=True)
        self.norm = stats.norm()
        self.var = []
        self.cdfs = []
    def gendata(self,num):
        self.var = random.multivariate_normal([0 for i in range(len(self.cov[0]))], self.cov,num)
        for i in self.var:
            for j in range(len(i)):
                i[j]= i[j]/math.sqrt(self.cov[j][j])
        self.cdfs = self.norm.cdf(self.var)
        data = [ [ np.percentile(self.data[:,j],100*i[j]) for j in range(len(i))] for i in self.cdfs ]
        return data

if __name__ == "__main__":
    r = np.random.rand(2,3)
    copula = Copula(r)
    a = copula.gendata(3)
    print(a)


   



