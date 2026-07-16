class Product:
    def __init__(self, product_id, product_name, price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def add_stock(self, qty):
        self.stock += qty

    def reduce_stock(self, qty):
        if qty > self.stock:
            raise Exception("Not enough stock available")
        self.stock -= qty

    def display_product(self):
        print(self.product_id, self.product_name, self.price, self.stock)


p = Product(101, "Mouse", 499, 20)
p.display_product()
p.reduce_stock(21)
p.display_product()