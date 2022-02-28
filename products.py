class Product:
    def __init__(self):
        self.name = "name"
        self.price = "price"
        self.category = "category"

    def update_price(self, percent_change, is_increased):
        if is_increased > 0:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)

    def print_info(self):
        print(self.category)
