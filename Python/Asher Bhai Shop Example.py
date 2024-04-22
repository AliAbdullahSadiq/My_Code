class item:
    def __init__(self, price, quantity, discount, order):
        self.price = price
        self.quantity = quantity
        self.discount = discount/100
        self.order = order

    def get_stock(self, quantity):
        return self.quantity

    def get_price(self, price):
        return self.price

    def get_invoice(self, price, quantity, discount):
        print()

    def update_stock(self):
        self.quantity -= self.order

    def discount(self, price, discount):
        if self.order >= 10:
            self.price = price * (discount/100)

    def get_sale(self):
        if self.order >= 10:
            return self.price * self.discount
        else:
            return self.price

item1 = item(4, 50, 1, 10)
item2 = item(4, 50, 2, 10)
item3 = item(4, 50, 3, 10)
item4 = item(4, 50, 4, 10)
item5 = item(4, 50, 5, 10)
item6 = item(4, 50, 6, 10)