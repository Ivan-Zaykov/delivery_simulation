class Supplier:
    def __init__(self, name):
        self._name = name
        self._stock = {
            "Pizza": 1000,
            "Soda": 2000,
            "Banana": 3000,
        }
        print(f"Инициализирован поставщик `{self._name}`")

    def deliver_goods(self, goods):
        print(f"Поставщик `{self._name}`: необходимо доставить товары: {goods}")
        available_items = {}
        for item, qty in goods.items():
            if self._stock.get(item, 0) >= qty:
                available_items[item] = qty
                self._stock[item] -= qty
            else:
                available_items[item] = self._stock.get(item, 0)
                self._stock[item] = 0
        print(f"Поставщик `{self._name}`: доставляются товары: {available_items}")
