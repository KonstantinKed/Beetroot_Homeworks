

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:

    def __init__(self):
        self.product_store = []
        self.rate = 1.3
        self.premium_price = 0
        self.amount = 0
        self.income = 0

    def add(self, product, amount: int):
        self.premium_price = round((product.price*self.rate), 3)
        product.amount = int(amount)
        product.price = self.premium_price
        self.product_store.append(product)
        return self.product_store

    def set_discount(self, identifier, percent, identifier_type="name"):
        print('\nSET DISCOUNT')
        print('===================')
        for product in self.product_store:
            if product.name == identifier or product.type == identifier_type:
                if percent >= 100:
                    raise ValueError("Discount is greater than the product price")
                else:
                    product.price = product.price*((100-percent)/100)
            return (f'{product.type}\t{product.name.strip()}\t{product.amount}\t{product.price}')

    def sell_product(self, product_name, amount: int):

        for product in self.product_store:
            if product.name.strip() == product_name:
                if product.amount > int(amount):
                    print('\nSELL PRODUCT')
                    print('===================')
                    product.amount -= int(amount)
                    self.income = amount * product.price
                else:
                    raise ValueError("You try to sell more products than available in store")
                return (f'{int(amount)}\t{product.name.strip()} was sold. Remaining amount is: {product.amount}')

    def get_income(self):
        print('\nINCOME of ProductStore')
        print('===================')
        return (f'Total income of the store is: {self.income}')

    def get_all_products(self):
        print("TYPE\t\tNAME\t\tAMOUNT\tPRICE")
        print('===================')
        for item in self.product_store:
            print(f'{item.type}\t{item.name}\t{item.amount}\t{item.price}')

    def get_product_info(self, product_name):
        print("\nGET PRODUCT INFO")
        print('===================')
        for item in self.product_store:
            if item.name.strip() == product_name.strip():
                return item.name.strip(), item.amount

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', '      Ramen       ', 1.5)
p3 = Product('Game', 'PlayStation 5   ', 1000)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.add(p3, 20)
s.get_all_products()
print(s.set_discount(p.name, 10))   # try 100 to raise ValueError
print(s.get_product_info("Ramen"))
print(s.sell_product("Ramenfdff", 100))
print(s.sell_product("PlayStation 5", 5))
print(s.sell_product("PlayStation 5", 10.5))  # try 16 to raise ValueError
print(s.get_income())