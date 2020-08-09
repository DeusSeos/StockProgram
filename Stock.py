from yahoo_fin import stock_info as si
import time
import datetime as dt
import yaml

class stock():
    def __init__(self, company, ticker):
        self.name = company
        self.ticker = ticker
        self.priceList = {}
        """Stock should hold stock prices throughout the day"""

    def get_price(self):
        """gets current time and stock's current price appends to dictionary of prices"""
        current_time = dt.datetime.now().time().isoformat(timespec='seconds')
        current_price = si.get_live_price(self.ticker)
        self.priceList[current_time] = current_price # sets time with the current price at that time
        return "{}{}{}".format(current_time, '-' * 15, current_price)

    def get_list(self):
        return self.priceList



if __name__ == '__main__':
    amdStock = stock('AMD', 'AMD')
    for i in range(2):
        print(i)
        amdStock.getPrice()
        time.sleep(1)
    print(amdStock.priceList)
    amdStock.saveStock()
