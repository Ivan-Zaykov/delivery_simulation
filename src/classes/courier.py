import math
import time
from .worker import Worker
from src.utils.constants import Constants


class Courier(Worker):
    def __init__(self, name, store_coords=(50, 50)):
        super().__init__(name)
        self._store_coords = store_coords

    def deliver_order(self):
        print(f"Курьер `{self.name}` забрал заказ {self._current_order.id}.")
        distance = math.sqrt(
            (self._current_order.customer.address[0] - self._store_coords[0]) ** 2 +
            (self._current_order.customer.address[1] - self._store_coords[1]) ** 2
        )
        delivery_time = distance / Constants.courierSpeed() + Constants.oneMinute() + Constants.oneMinute()
        print(f"Курьер `{self.name}` доставляет заказ {self._current_order.id}. /"
              f"Время: {delivery_time / Constants.TIME_COMPRESSION_RATIO / Constants.SECONDS_PER_MINUTE:.2f} минут.")
        time.sleep(delivery_time)
        print(f"Курьер `{self.name}` доставил заказ {self._current_order.id}.")

        self._current_order = None
