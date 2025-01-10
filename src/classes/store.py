from .storekeeper import Storekeeper
from .courier import Courier


class Store:
    def __init__(self, name):
        self.name = name
        self.stock = {}  # Словарь: товар -> количество
        self.orders = []  # Очередь заказов
        self.order_counter = 0  # Счётчик для уникальных ID заказов
        self.workers = []  # Все работники
        print(f"Инициализирован склад `{self.name}`")

    def update_stocks(self, goods):
        print(f"Склад `{self.name}`: обновляет стоки товаров: {goods}")
        for item, qty in goods.items():
            if item in self.stock:
                self.stock[item] += qty
            else:
                self.stock[item] = qty
            print(f"Склад `{self.name}`: добавлено {qty} единиц товара '{item}'")

    def process_order(self, order):
        print(f"Склад `{self.name}`: получен заказ {order}")

        self.order_counter += 1
        order.id = self.order_counter
        print(f"Склад `{self.name}`: заказу назначен id {self.order_counter}")
        self.orders.append(order)

        available_items = {}
        for item, qty in order.items.items():
            if self.stock.get(item, 0) >= qty:
                available_items[item] = qty
                self.stock[item] -= qty
            else:
                available_items[item] = self.stock.get(item, 0)
                self.stock[item] = 0
        order.items = available_items  # Обновляем заказ
        print(f"Склад `{self.name}`: заказ {order.id} готов к сборке: {order.items}")

        self.assign_storekeeper(order)
        self.assign_courier(order)

    def assign_storekeeper(self, order):
        storekeeper = next((w for w in self.workers if isinstance(w, Storekeeper) and w.is_available()), None)
        if storekeeper:
            storekeeper.assign_order(order)
        else:
            print(f"Склад: нет доступных сборщиков для заказа {order.id}.")

    def assign_courier(self, order):
        courier = next((w for w in self.workers if isinstance(w, Courier) and w.is_available()), None)
        if courier:
            courier.deliver_order(order)
        else:
            print(f"Склад: нет доступных курьеров для заказа {order.id}.")
