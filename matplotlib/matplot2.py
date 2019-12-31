list_year = [
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017
]

list_gdp = [
    219438.50,
    270232.30,
    319515.50,
    349081.40,
    413030.30,
    489300.20,
    542343.23,
    591239.34,
    643934.45,
    682345.35,
    742455.32,
    825829.94
]

list_gdp_growth = [
    12.70,
    14.20,
    9.70,
    9.40,
    10.60,
    9.50,
    7.90,
    7.80,
    7.30,
    6.90,
    6.70,
    6.90
]

import matplotlib.pyplot as plt

plt.bar(list_year, list_gdp)

plt.plot(list_year, list_gdp_growth, color='red')

plt.title("gdp amount / growth from 2006 to 2017")

plt.xlabel('year')

plt.ylabel('gdp amount / growth')

plt.show()