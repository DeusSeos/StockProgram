class DateNotInPortfolio(Exception):
    """
    Exception raised when date is not in dictionary of a ticker
    Attributes:
        - date
        -
    """
    def __init__(self, datetime, message = "Datetime is not in the ticker's dictionary"):
        self.datetime = datetime
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.datetime} -> {self.message}'


class StockNotInPortfolio(Exception):
    """
    Exception raised when ticker is not in the portfolio
    Attributes:
        - ticker
        - message
    """
    def __init__(self, ticker, message="Ticker is not in Portfolio"):
        self.ticker = ticker
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.ticker} -> {self.message}'

