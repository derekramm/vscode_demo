class OrderLine:
    def __init__(self, name, price, count):
        self.__name, self.__price, self.__count = name, price, count
        self.__subtotal = self.__price * self.__count
    def subtotal(self): return self.__subtotal

class Order:
    def __init__(self):
        self.__orderlines, self.__grandtotal = [], 0
    def orderlines(self): return tuple(self.__orderlines)
    def grandtotal(self): return self.__grandtotal
    def add_orderline(self, orderline):
        self.__orderlines.append(orderline)
        self.__grandtotal += orderline.subtotal
    def remove_orderline(self, orderline):
        self.__orderlines.remove(orderline)
        self.__grandtotal -= orderline.subtotal