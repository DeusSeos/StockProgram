import Utils

"""Main class will create a config file"""

"""How to display information:
    Portfolio based:
    Fractional Stocks?
    Buy and Sell functions
   Code:
    Portfolio Object
    Portfolio manager
    Window display
    Grapher
"""


def display_menu():
    """Diqsplay menu for the program"""
    choices = ("1. Add stock", "2. Remove stock", "3. Get open price", "4. Get close price")
    for item in choices:
        print(item)


if __name__ == '__main__':
    print("Welcome to Dominic's Stock Program")
    display_menu()
    print(Utils.valid_file_name("1.txt"))
