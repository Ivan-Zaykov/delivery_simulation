import math
import time
from .worker import Worker
from src.utils.constants import Constants


class Courier(Worker):
    def __init__(self, name, store_coords=(50, 50)):
        super().__init__(name)
        self.current_order = None
        self.store_coords = store_coords

    def deliver_order(self, order):
        self.current_order = order
        self.is_available = False
        print(f"Курьер `{self.name}` забрал заказ {order.id}.")
        distance = math.sqrt(
            (order.customer.address[0] - self.store_coords[0]) ** 2 +
            (order.customer.address[1] - self.store_coords[1]) ** 2
        )
        delivery_time = distance / Constants.courierSpeed() + Constants.oneMinute() + Constants.oneMinute()
        print(f"Курьер `{self.name}` доставляет заказ {order.id}. /"
              f"Время: {delivery_time / Constants.TIME_COMPRESSION_RATIO / Constants.SECONDS_PER_MINUTE:.2f} минут.")
        time.sleep(delivery_time)
        print(f"Курьер `{self.name}` доставил заказ {order.id}.")
        self.is_available = True
