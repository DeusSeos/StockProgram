from yahoo_fin import stock_info as si
import time
import datetime as dt
import yaml

class stock():
    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker
        self.fileName = name + ".yml"
        self.priceList = []
        """Stock should hold current date with a dictionary of times and stock prices at those times"""

    def getPrice(self):
        """gets current time and stock's current price appends to dictionary of prices"""
        currentTime = dt.datetime.now().time().isoformat(timespec='seconds')
        currentPrice = str(round(si.get_live_price(self.ticker), 2))
        set = {}
        set[currentTime] = currentPrice
        self.priceList.append(set)
        return "{}{}{}".format(currentTime, '-' * 15, currentPrice)

    def printDict(self):
        print(self.priceDict)

    def saveStock(self):
        with open(self.fileName, 'a') as file:
            yaml.dump(self.priceList, file)


if __name__ == '__main__':
    amdStock = stock('AMD', 'AMD')
    for i in range(2):
        print(i)
        amdStock.getPrice()
        time.sleep(1)
    print(amdStock.priceList)
    amdStock.saveStock()
