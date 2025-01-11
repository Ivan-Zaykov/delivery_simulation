import time
from .worker import Worker
from src.utils.constants import Constants


class Storekeeper(Worker):
    def collect_order(self):
        print(f"Сборщик `{self.name}` начал сборку заказа {self._current_order.id}.")
        time.sleep(len(self._current_order.items) * Constants.orderAssemblyTime())
        print(f"Сборщик `{self.name}` завершил сборку заказа {self._current_order.id}.")

        self._current_order = None
