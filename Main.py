"""Main class will create a config file"""

def displayMenu():
    choices = ("1. Add stock", "2. Remove stock", "3. Get open price", "4. Get close price")
    for item in choices:
        print(item)

if __name__ == '__main__':
    print("Welcome to Dominic's Stock Program")
    displayMenu()