import pandas as pd

df = pd.read_csv('infor.csv')
# print(df)
sf = pd.read_csv("information.csv")
# print(sf)

data = pd.merge(df, sf, on="order_id", how="inner")
print(data.head())