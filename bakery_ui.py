import tkinter
from tkinter import *

class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        label = Label(window, text='샌드위치 (5000원)').grid(column=0, row=0)
        label = Label(window, text='케이크 (20000원)').grid(column=0, row=1)
        self.send = Entry(window, width=10)
        self.send.grid(column=1, row=0)
        self.cake = Entry(window, width=10)
        self.cake.grid(column=1, row=1)
        order = Button(window, text="주문하기", command=self.send_order).grid(column=0, row=3)

    def send_order(self):
        num1 = self.send.get()
        num2 = self.cake.get()
        if num1.isdigit() == True:
            if int(num1) > 0:
                num1 = int(num1)
            else:
                num1 = None
        else:
            num1 = None
        if num2.isdigit() == True:
            if int(num2) > 0:
                num2 = int(num2)
            else:
                num2 = None
        else:
            num2 = None
        if num1 != None and num2 != None:
            order_text = "{}: 샌드위치 (5000원) {}개, 케이크 (20000원) {}개".format(self.name,num1,num2)
            self.bakeryView.add_order(order_text)
        elif num1 == None and num2 != None:
            order_text = "{}: 케이크 (20000원) {}개".format(self.name, num2)
            self.bakeryView.add_order(order_text)
        elif num1 != None and num2 == None:
            order_text = "{}: 샌드위치 (5000원) {}개".format(self.name, num1)
            self.bakeryView.add_order(order_text)
        else:
            return 0

if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
