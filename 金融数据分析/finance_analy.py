import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = ts.get_k_data("601318", "1990-03-01", "2020-11-03")
# print(df)

"""
数据是平安的数据
练习：
使用pandas包计算该股票历史数据的5日均线和10日均线
使用matplotlab包可视化历史数据的收盘价和两条均线
分析输出所有金叉和死叉日期
如果我从2010开始，初始资金100000，金叉尽量买入，死叉全部卖出，到今天为止，我的收益如何？
"""
# 方法一
# df['ma5'] = np.nan
# # print(df)
# for i in range(4, len(df)):
#     df.loc[i, "ma5"] = df['open'][i-4:i+1].mean()
# print(df)
# 方法二
# print(df['open'].rolling(5).mean())
df['ma5'] = df['open'].rolling(5).mean()
df['ma10'] = df['open'].rolling(10).mean()
# print(df)

"""
数据可视化
"""
# 方法一
# plt.plot(df['close'])
# plt.plot(df['ma5'])
# plt.plot(df['ma10'])
# plt.show()
# 方法二
# outer = df[['close','ma5','ma10']].iloc[:100,:].plot()
# print(outer.show())


"""
df = df.dropna()
# print(df)
golden = []
death = []

for i in range(len(df.index)):
    if df.loc[df.index[i], 'ma5'] <= df.loc[df.index[i], 'ma10'] and df.loc[df.index[i-1], 'ma5'] > df.loc[df.index[i-1], 'ma10']:
        death.append(i)
    if df.loc[df.index[i], 'ma5'] >= df.loc[df.index[i], 'ma10'] and df.loc[df.index[i-1], 'ma5'] < df.loc[df.index[i-1], 'ma10']:
        golden.append(i)
print(df.iloc[golden,:]['date'])
print(df.iloc[death,:]["date"])

"""




"""
FF ----> golden
TT ----> death
"""
df = df.dropna()
df.index = pd.to_datetime(df['date'])
df = df["2010":]

del df['date']
# print(df)
# golden = df[~(sr1 | ((~sr1).shift(1)))]
# print(df[~(sr1 | ((~sr1).shift(1)))]['date'])
# death = df[sr1 & ((~sr1).shift(1))]
# print(death)
# print(golden)
# print(death)
sr1 = df['ma5'] < df["ma10"]
golden = df[~(sr1 | ((~sr1).shift(1)))].index
# print(df[~(sr1 | ((~sr1).shift(1)))]['date'])
death = df[sr1 & ((~sr1).shift(1))].index

# print(golden)
# print(death)

"""
策略
"""

begin_money = 100000
money =begin_money
hold = 0

ss = pd.Series(1, index=golden).append(pd.Series(0, index=death)).sort_index()
print(ss)

for i in ss.index:
    p = df.loc[i, 'open']
    if ss[i] == 1:
        to_buy = money // (100 * p)  * 100
        money -= to_buy * p
        hold += to_buy
    else:
        money += hold * p
        hold = 0

now_values = money + df['open'].iloc[-1]*hold
print(now_values)


        
