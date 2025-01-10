class Supplier:
    def __init__(self, name):
        self.name = name
        self.stock = {
            "Pizza": 1000,
            "Soda": 2000,
            "Banana": 3000,
        }
        print(f"Инициализирован поставщик `{self.name}`")

    def deliver_goods(self, goods):
        print(f"Поставщик `{self.name}`: необходимо доставить товары: {goods}")
        available_items = {}
        for item, qty in goods.items():
            if self.stock.get(item, 0) >= qty:
                available_items[item] = qty
                self.stock[item] -= qty
            else:
                available_items[item] = self.stock.get(item, 0)
                self.stock[item] = 0
        print(f"Поставщик `{self.name}`: доставляются товары: {available_items}")


