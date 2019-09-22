# made by Ajay_Luo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import scipy.stats as scs
import statsmodels.api as sm
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']


def plot_all(df):
    df = pd.DataFrame(df)
    n = int(np.sqrt(len(df.columns))) + 1
    fig, axes = plt.subplots(n, n)
    plt.subplots_adjust(hspace=0.4)
    if n > 1:
        for j in range(len(df.columns)):
            i = j // n
            k = j % n
            data = df.iloc[:, j].copy()
            axes[i, k].plot(data)
            axes[i, k].set_title(df.columns[j])
    if n == 1:
        data = df.iloc[:, 0].copy()
        axes[0].plot(data)
        axes[0].set_title(df.columns[0])
    return fig


def return_standard_normal_test(df):
    df = pd.DataFrame(df)
    n = int(np.sqrt(len(df.columns))) + 1
    # n = 2
    fig, axes = plt.subplots(n, 2*n)
    plt.subplots_adjust(hspace=0.4)
    if n > 1:
        for j in range(len(df.columns)):
            i = j // n
            k = j % n
            data = df.iloc[:, j].copy()
            data = data / data.shift(1) - 1
            data.dropna(inplace=True)
            d_score, possible = scs.kstest(data, 'norm')
            axes[i, 2*k].hist(data, bins=70, density=1)
            x = np.linspace(axes[i, 2*k].axis()[0], axes[i, 2*k].axis()[1])
            axes[i, 2*k].plot(x, scs.norm.pdf(x, loc=data.mean(), scale=data.std()))
            sm.qqplot(data, line='s', ax=axes[i, 2*k+1])
            axes[i, 2*k+1].set_xlabel("")
            axes[i, 2*k].set_title(df.columns[j])
            axes[i, 2*k + 1].set_title(f"ks值为{d_score.round(2)},P值为{possible.round(2)}")
        return fig
    if n == 1:
        data = df.iloc[:, 0].copy()
        data = data / data.shift(1) - 1
        data.dropna(inplace=True)
        d_score, possible = scs.kstest(data, 'norm')
        axes[0].hist(data, bins=70, density=1)
        x = np.linspace(axes[0].axis()[0], axes[0].axis()[1])
        axes[0].plot(x, scs.norm.pdf(x, loc=data.mean(), scale=data.std()))
        sm.qqplot(data, line='s', ax=axes[1])
        axes[0].set_title(df.columns[0])
        axes[1].set_title(f"ks值为{d_score.round(2)},P值为{possible.round(4)}")
        return fig


def log_df(df):
    df = df.apply(lambda x: np.log(x))
    return df


def main():
    df = pd.read_excel(path)
    df.index = df["timestamp"]
    df.drop(["timestamp"], inplace=True, axis=1)
    df.dropna(inplace=True)
    # df = log_df(df)
    plot_all(df)
    return_standard_normal_test(df)
    # for symbol in df.columns:
    #     print(symbol)
    #     return_standard_normal_test(df[symbol])
    df_m = df.resample("M").last()
    return_standard_normal_test(df_m)
    plt.show()
    plt.savefig('test.jpg')


if __name__ == '__main__':
    path = './申万.xlsx'
    main()
