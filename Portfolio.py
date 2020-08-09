import datetime as dt
import yaml

class Portfolio:
    """
    Portfolio holds a dictionary with the stocks that have been bought and the date bought.
    Saves to file upon buy or sell
    """

    def __init__(self, filename = "portfolio.yml"):
        self.filename = filename
        self.stocks = {}

    def buy(self, ticker, amount):
        if ticker in self.stocks:
            self.stocks[ticker].append({dt.datetime.now().isoformat(): amount})
        else:
            self.stocks[ticker] = [{dt.datetime.now().isoformat(): amount}]

    def save(self):
        with open(self.filename) as file:
            yaml.dump(self.stocks, file)

    def get_stocks(self):
        return self.stocks


if __name__ == '__main__':
    a = Portfolio()
    a.buy("AMD", 2)
    a.buy("AMD", 5)
    print(a.get_stocks())