from .storekeeper import Storekeeper
from .courier import Courier
import prompt


class Store:
    def __init__(self, name):
        self._name = name
        self._stock = {}  # Словарь: товар -> количество
        self._orders = {}  # Словарь: id заказа -> состав
        self._order_counter = 0  # Счётчик для уникальных ID заказов
        self._workers = []  # Все работники
        print(f"Инициализирован склад `{self._name}`")

    @property
    def stock(self):
        return self._stock

    @property
    def orders(self):
        return self._orders

    @property
    def workers(self):
        return self._workers

    def update_stocks(self, goods):
        print(f"Склад `{self._name}`: обновляет стоки товаров: {goods}")
        for item, qty in goods.items():
            if item in self._stock:
                self._stock[item] += qty
            else:
                self._stock[item] = qty
            print(f"Склад `{self._name}`: добавлено {qty} единиц товара '{item}'")

    def process_order(self, order):
        self.assign_order_id_and_items_count(order)

        storekeeper = self.assign_storekeeper(order)
        if storekeeper:
            storekeeper.execute_work()
        else:
            print(f"Склад: нет доступных сборщиков для заказа {order.id}.")

        courier = self.assign_courier(order)
        if courier:
            courier.execute_work()
        else:
            print(f"Склад: нет доступных курьеров для заказа {order.id}.")

    def assign_order_id_and_items_count(self, order):
        print(f"Склад `{self._name}`: получен заказ {order}")

        self._order_counter += 1
        order.id = self._order_counter
        print(f"Склад `{self._name}`: заказу назначен id {self._order_counter}")
        self._orders[order.id] = order

        available_items = {}
        for item, qty in order.items.items():
            unsufficient_qty = self.check_is_sufficient_count(item, qty)

            if unsufficient_qty:
                customer_agree_with_unsufficient = self.check_is_user_agree(item)

            if self._stock.get(item, 0) >= qty:
                available_items[item] = qty
                self._stock[item] -= qty
            elif unsufficient_qty:
                if customer_agree_with_unsufficient:
                    available_items[item] = self._stock.get(item, 0)
                    self._stock[item] = 0
                else:
                    pass
        order.items = available_items  # Обновляем заказ
        print(f"Склад `{self._name}`: заказ {order.id} готов к сборке: {order.items}")

    def assign_storekeeper(self, order):
        storekeeper = next((w for w in self._workers if isinstance(w, Storekeeper) and w.is_available()), None)
        if storekeeper:
            storekeeper.current_order = order
            return storekeeper
        else:
            return None

    def assign_courier(self, order):
        courier = next((w for w in self._workers if isinstance(w, Courier) and w.is_available()), None)
        if courier:
            courier.current_order = order
            return courier
        else:
            return None

    def check_is_sufficient_count(self, item, qty):
        store_count = self._stock[item]

        return qty > store_count

    def check_is_user_agree(self, item):
        is_agree = prompt.string("Вы согласны получить не полное количество товара " + item + "(yes/no): ")

        if is_agree == 'yes':
            return True
        elif is_agree == 'no':
            return False
        else:
            is_agree = prompt.string("Вы согласны получить не полное количество товара " + item + "(yes/no): ")

