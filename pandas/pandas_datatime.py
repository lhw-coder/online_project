import datetime
import numpy as np
import pandas as pd
import time
import dateutil
"""
时间序列
dateutil支持很多日期格式
"""
a = datetime.datetime.strptime("2010-10-01", "%Y-%m-%d")
# print(type(a))

b = dateutil.parser.parse("2010/10/01")
# print(type(b))

d = dateutil.parser.parse("01/01/2010")
# print(d)

f = dateutil.parser.parse("2010-01-01")
# print(f)

g = dateutil.parser.parse("2010 JAN 1st")
# print(g)


"""
批量处理时间对象
"""
c = pd.to_datetime(['2010/10/01','2010-08-09',"2010 JAN 1st","01/01/2010"])
# print(c)
# print(type(c))
# print(c.to_pydatetime())

sd = pd.Series([1,2,3], index=pd.to_datetime(['2010/10/01','2010-08-09',"2010 JAN 1st"]))
sf = pd.Series([1,2,3])
sf.index = pd.to_datetime(['2010/10/01','2010-08-09',"2010 JAN 1st"])
# print(sd)
# print(sf)

ll = pd.date_range("2018-01-01","2018-12-31", freq='MS')  # freq 频率 小时 3天 一周 产生时间序列 index对象 B：工作日
# print(ll)

pf = pd.read_csv('601318.csv')
# print(pf)

p_index = pd.to_datetime(pf['data'])
pf.index = p_index
print(pf)

"""
时间序列的特殊功能：
传入"年"/"年月"，作为切片的方式
传入日期范围作为切片方式

"""
print(pf["2008"])
print(pf["2008-03":])

kk = pf.index.strftime("%Y-%m-%d")
print(kk)

sd = pf.resample("2D").mean()  # 数据稀疏化 每三天取一个平均
print(sd)

gg = pf.resample("M").mean()   # 每个月取平均
print(gg)

fh = pf.resample("MS").first()  # 取每个月的第一天 last 最后一天
print(fh)

