import tushare as ts
import pandas as pd

df = ts.get_k_data("600519", "1990-03-01", "2020-11-03")


"""
测试数据是茅台的数据
练习一：
使用tushare包获取某股票的历史行情数据
输出该股票所有收盘比开盘上涨3%以上的日期
输出该股票所有开盘比前日收盘跌幅超过2%的日期
假如我从2010年1月1号开始，每月第一个交易日买入一手股票，每年最后一个交易日卖出所有股票，到今天，我的收益如何？
"""
sd = df[(df['close']- df['open']) / df['open'] > 0.03]['date']
# print(sd)
sr = df['close'].shift(1)
er = df[(df['open'] - sr) / sr < - 0.02]['date'].values


"""
策略
"""
df.index = pd.to_datetime(df['date'])
del df['date']
# print(df)
df = df['2010':]
# print(df)

df_monthly = df.resample('MS').first()
df_yearly = df.resample("A").last()

money = 0
hold = 0
for year in range(2010, 2020):
    # 买
    money -= df_monthly[str(year)]['open'].sum()*100
    hold += len(df_monthly[str(year)]) * 100

    # 卖
    if year != 2019:
        money += df_yearly[str(year)]['open'].iloc[0] * hold
        hold = 0

receive_money = hold * df['open'].iloc[-1]+money
print(receive_money)