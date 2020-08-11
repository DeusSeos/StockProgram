from yahoo_fin import stock_info as si
import yfinance as yf
import datetime as dt


class Stock:
    def __init__(self, company, ticker):
        self.name = company
        self.ticker = ticker
        self.priceList = {}
        """Stock should hold stock prices throughout the day"""

    def get_day_history(self):
        data = yf.download(tickers=self.ticker, period="1d", interval='1m')
        for time, price in zip(data.index.tolist(), data['Adj Close']):

            self.priceList[time.to_pydatetime()] = price

    def get_price(self):
        """gets current time and stock's current price appends to dictionary of prices || returns time and price"""
        current_time = dt.datetime.now().time().isoformat(timespec='seconds')
        current_price = si.get_live_price(self.ticker)
        self.priceList[current_time] = current_price # sets time with the current price at that time
        return "{}{}{}".format(current_time, '-' * 15, current_price)

    def get_list(self):
        return self.priceList


if __name__ == '__main__':
    amdStock = Stock('AMD', 'AMD')
    amdStock.get_day_history()
    print(amdStock.get_list())

