import pandas as pd

# pd.read_excel("601318.xlsx", sheet_name='601318')  # 后面的参数是那个sheet

# pd.read_table()


"""
重要参数
"""
# pd.read_csv("601318.csv", sep="\s+")

ss = pd.read_csv("601319.csv", header=None, names=list("abcdef"))
# print(ss)

sd = pd.read_csv("601318.csv", index_col="data").index   # 索引  这个索引是字符串不是对象类型
# print(sd)

dd = pd.read_csv("601318.csv", index_col="data", parse_dates=True)  # 这个是对象
# print(dd)

# 把数据异常的地方指定为缺失值
sr = pd.read_csv("601318.csv", index_col="data", parse_dates=True, na_values=["None", "false", "", "@"])

del dd['id']
print(dd)

dd.to_csv("test.csv",sep=';', float_format="%.3f", index=False, header=None, na_rep="None")  # 去掉行索引


