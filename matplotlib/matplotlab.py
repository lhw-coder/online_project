import matplotlib.pyplot as plt

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
    2017,
    2018,
    2019
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
    825829.94,
    862312.56,
    933423.66
]

plt.bar(list_year, list_gdp)

plt.title("gdp amount from 2006 to 2019")

plt.xlabel("year")

plt.ylabel("gdp amount")

plt.show()

plt.plot(list_year, list_gdp)

plt.title('gdp amount from 2006 to 2019')

plt.xlabel("year")

plt.ylabel("gdp amount")

plt.show()

gdp_2017 = {
    "primary industry": 65468,
    "secondary industry": 334623,
    "tertiary industry": 427032
}

labels = gdp_2017.keys()
values = gdp_2017.values()

plt.pie(values,
        labels=labels,
        autopct="%.1f%%",
        startangle=90
        )

plt.axis("equal")

plt.legend()

plt.show()