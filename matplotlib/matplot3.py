"""
画双坐标图形
"""

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

fig = plt.figure(figsize=(8, 6))

ax1 = fig.add_subplot(1,1,1)
ax1.bar(list_year, list_gdp, label="gdp amount")
ax1.legend(loc="upper left")
ax1.set_xlabel("year")
ax1.set_ylabel("gdp amount")

ax2 = ax1.twinx()
ax2.plot(list_year, list_gdp_growth, color = 'red', label="gdp growth")
ax2.legend(loc="upper right")
ax2.set_ylabel("gdp growth")
ax2.set_ylim(0, 20)

plt.title("gdp amount / growth from 2006 to 2017")

plt.show()


fig1 = plt.figure(figsize=(8, 6))

ax3 = fig1.add_subplot(2, 1, 1)
ax3.bar(list_year, list_gdp, label="gdp amount")
ax3.legend(loc="upper left")
ax3.set_ylabel("gdp amount")
ax3.set_xlabel("year")
ax3.set_title("gdp amount from 2006 to 2017")

ax4 = fig.add_subplot(2, 1, 2)
ax4.plot(list_year, list_gdp_growth, color = "red", label="gdp growth")
ax4.legend(loc="upper right")
ax4.set_ylabel("gdp growth")
ax4.set_ylim(0,15)
ax4.set_title("gdp growth from 2006 to 2017")
ax4.grid(True)

plt.tight_layout()

plt.show()