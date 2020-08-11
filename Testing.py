import yaml
import sys
import time
from screeninfo import get_monitors
from pandas import DataFrame
from Stock import Stock
import matplotlib.pyplot as plt
import yfinance
import pandas as pd
from Portfolio import Portfolio


# """Works!"""
# testPortfolio = Portfolio()
# testPortfolio.buy("AMD", 2)
# time.sleep(1)
# testPortfolio.buy("AAPL", 1)
# time.sleep(1)
# testPortfolio.buy("INTL", 3)
# testPortfolio.save()


# """Works!!!"""
# stock = Stock("AMD", "AMD")
# stock.get_day_history()
# data = {"Time": [], "Price": []}
# for k, v in stock.get_list().items():
#     data["Time"].append(k)
#     data["Price"].append(v)
# df = pd.DataFrame(data=data, columns=["Time", "Price"]) #pd is import pandas as pd
# df = df[['Time', 'Price']].groupby('Time').sum()
# df.plot(kind='line', legend=True, color='r',marker='o', fontsize=10)
# plt.show()


#
# """Works!!!"""
# data = yfinance.download("AMD", period='1d', interval='60m')
# print(data.columns.tolist())
# print(data.index.tolist()) #returns the datetime
# for elem in data.index.tolist():
#     print(type(elem))
#     print(elem.to_pydatetime())
#     print(type(elem.to_pydatetime()))
#     break
#     print(str(elem)[:-6]) #returns only the time data is fetched


# """Works!!!"""
# stock = Stock("AMD", "AMD")
# for i in range(10):
#     stock.get_price()
#     time.sleep(1)
# data = {"Time": [], "Price": []}
# for k, v in stock.get_list().items():
#     data["Time"].append(k)
#     data["Price"].append(v)
# df1 = DataFrame(data=data, columns=['Time', 'Price'])
# print(df1)


#"""Works!!!"""
#
# width = 100000
# height = 100000
# for m in get_monitors():
#     if width > int(m.width):
#         width = int(m.width)
#     if height > int(m.height):
#         height = int(m.height)
# print(height)
# print(width)


# """Works!!!"""
# for m in get_monitors():
#     print(m.width)


# """Works!!!"""
# testStock = [{'AMD': {"11/01/20": "1"}}]
# with open("test.yml", 'a') as file:
#     yaml.dump(testStock, file)