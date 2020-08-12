import datetime as dt
import yaml
import Utils
from Errors import *



class Portfolio:
    """
    Portfolio holds a dictionary with the stocks that have been bought and the date bought.
    Save to file upon buy or sell
    """

    def __init__(self, filename="portfolio.yml"):
        self.filename = filename
        self.stocks = {}
        if Utils.file_exists(self.filename):
            self.load()

    def buy(self, ticker, amount):
        if ticker in self.stocks:
            self.stocks[ticker][dt.datetime.now()] = amount
        else:
            self.stocks[ticker] = {dt.datetime.now(): amount}

    def sell(self, ticker, datetime, amount) -> bool:
        if ticker in self.stocks:  # If we have the stock
            stocks = self.stocks[ticker]
            if datetime in stocks:
                if stocks[datetime] > amount:  # if amount asking to be sold is less than held
                    stocks[datetime] -= amount
                elif stocks[datetime] == amount:  # if amount asking to be sold is equal to held
                    stocks.pop(datetime)
                else:  # if amount asking to be sold is greater than held
                    stocks.pop(datetime)
            else:
                raise DateNotInPortfolio(datetime=datetime)
        else:
            raise StockNotInPortfolio(ticker=ticker)

    def load(self):
        """Load will move all of the data stored in the file to the object"""
        with open(self.filename, 'r') as file:
            self.stocks = yaml.load(file, yaml.FullLoader)

    def save(self):
        """Save dumps all of the data in dictionary to file"""
        with open(self.filename, 'w') as file:
            yaml.dump(self.stocks, file)

    def get_stocks(self):
        return self.stocks.keys()


if __name__ == '__main__':
    a = Portfolio()
    print(a.get_stocks())
    # dictionary = a.get_stocks()['AMD']
    # for key, value in dictionary.items():
    #     print(key, value)
    # try:
    #     a.sell('AMD', dt.datetime(2021, 8, 11, 14, 24, 1, 968544), 1)
    # except Exception as ex:
    #     print(ex)


    # print(a.get_stocks())
    # tempList = a.get_stocks()['AMD']
    # # print(a.get_stocks()['AMD'])
    # keyList = tempList.keys()
    # print(keyList)
