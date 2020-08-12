import Utils

"""Main class will create a config file"""

"""How to display information:
    Portfolio based:
    Fractional Stocks? <- No for now
    Buy and Sell functions <- Completed
   Code:
    Portfolio Object <- Completed
    Portfolio manager <- Probably don't need TBD
    Window display
    Grapher
"""


def display_menu():
    """Display menu for the program"""
    choices = ("1. Add stock", "2. Remove stock", "3. Get open price", "4. Get close price")
    for item in choices:
        print(item)


if __name__ == '__main__':
    print("Welcome to Dominic's Stock Program")
    display_menu()
    print(Utils.valid_file_name("1.txt"))
