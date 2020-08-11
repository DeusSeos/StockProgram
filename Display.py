from tkinter import *
from Stock import Stock
from screeninfo import get_monitors


class Display(Frame):

    def __init__(self, stocklist, master=None):
        Frame.__init__(self, master)
        self.stocklist = stocklist
        self.size = len(stocklist)
        self.master = master
        self.init_window()
        self.create_menu()

    def init_window(self):
        self.master.title('Stock Program')
        self.pack(fill=BOTH, expand=1)
        self.master.iconphoto(True, PhotoImage(file="StockIconTest2.png"))

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
        for n in range(len(self.stocklist)):
            sell.add_command(label="A")
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
    width = 100000
    height = 100000
    for m in get_monitors():
        if width > int(m.width):
            width = int(m.width)
        if height > int(m.height):
            height = int(m.height)
    resolution = str(width) + "x" + str(height)
    root.geometry(resolution)
    a = [Stock("Advanced Mirco Devices", 'AMD')]
    app = Display(stocklist=a, master=root)
    root.mainloop()

