import time
from .worker import Worker
from src.utils.constants import Constants


class Storekeeper(Worker):
    def assign_order(self, order):
        print(f"Сборщик `{self.name}` начал сборку заказа {order.id}.")
        time.sleep(len(order.items) * Constants.orderAssemblyTime())
        print(f"Сборщик `{self.name}` завершил сборку заказа {order.id}.")
