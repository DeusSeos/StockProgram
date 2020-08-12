from tkinter import *
from Utils import *
from Portfolio import *


class Display(Frame):

    def __init__(self, stocklist, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.stocklist = stocklist
        self.size = len(stocklist)
        self.init_window()
        self.create_menu()

    def init_window(self):
        self.master.title('Stock Program')
        self.pack(fill=BOTH, expand=1)
        #self.master.iconphoto(True, PhotoImage(file="StockIconTest2.png"))
        try:
            self.master.geometry(getResolution())
        except AttributeError as ex:
            print(ex)

    def create_menu(self):
        """
        Creates the menu bar and adds the different buttons
        Create Portfolio cascade menu
        Buy Stock -> create new window to buy stock?
        Sell Stock
        Load Portfolio
        Save Portfolio
        """
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        portfolio = Menu(menubar, tearoff=0)
        portfolio.add_command(label="Buy")

        sell = Menu(portfolio, tearoff=0)
        for stockName in self.stocklist:
            sell.add_command(label=stockName)
        sell.add_separator()

        portfolio.add_cascade(label="Sell", menu=sell)
        portfolio.add_separator()
        portfolio.add_command(label='Load')
        portfolio.add_command(label='Save')
        menubar.add_cascade(label="Portfolio", menu=portfolio)

    def client_exit(self):
        exit()


if __name__ == '__main__':
    root = Tk()
    a = Portfolio().get_stocks()
    app = Display(stocklist=a, master=root)
    root.mainloop()

