from .storekeeper import Storekeeper
from .courier import Courier


class Store:
    def __init__(self):
        self.stock = {}  # Словарь: товар -> количество
        self.orders = []  # Очередь заказов
        self.workers = []  # Все работники
        self.providers = []  # Все поставщики

    def add_stock(self, item, quantity):
        if item in self.stock:
            self.stock[item] += quantity
        else:
            self.stock[item] = quantity
        print(f"Склад: добавлено {quantity} единиц товара '{item}'.")

    def process_order(self, order):
        print(f"Склад: получен заказ {order.id} от {order.customer}")
        available_items = {}
        for item, qty in order.items.items():
            if self.stock.get(item, 0) >= qty:
                available_items[item] = qty
                self.stock[item] -= qty
            else:
                available_items[item] = self.stock.get(item, 0)
                self.stock[item] = 0
        order.items = available_items  # Обновляем заказ
        print(f"Склад: заказ {order.id} готов к сборке: {order.items}")

    def assign_storekeeper(self, order):
        storekeeper = next((w for w in self.workers if isinstance(w, Storekeeper) and w.is_available), None)
        if storekeeper:
            storekeeper.assign_order(order)
        else:
            print(f"Склад: нет доступных сборщиков для заказа {order.id}.")

    def assign_courier(self, order):
        courier = next((w for w in self.workers if isinstance(w, Courier) and w.is_available), None)
        if courier:
            courier.deliver_order(order)
        else:
            print(f"Склад: нет доступных курьеров для заказа {order.id}.")

    def registerProvider(self, provider):
        self.providers.append(provider)

    def requestProductsFromProviders(self, product, quantity):
        """
        Заказывает товар у поставщиков.

        :param product: str - название товара
        :param quantity: int - количество, которое нужно заказать
        """
        for provider in self.providers:
            if quantity <= 0:
                break
            delivered = provider.deliver(product, quantity)
            self.add_stock(product, delivered)
            quantity -= delivered

        if quantity > 0:
            print(f"Недостаточно {product} у поставщиков, осталось заказать: {quantity}")
