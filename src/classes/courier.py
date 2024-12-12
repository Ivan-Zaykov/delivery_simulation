import math
import time
from .worker import Worker

class Courier(Worker):
    def __init__(self, name, warehouse_coords=(50, 50)):
        super().__init__(name)
        self.current_order = None
        self.warehouse_coords = warehouse_coords

    def deliver_order(self, order):
        self.current_order = order
        self.is_available = False
        print(f"Курьер {self.name} забрал заказ {order.id}.")
        distance = math.sqrt(
            (order.customer.address[0] - self.warehouse_coords[0]) ** 2 +
            (order.customer.address[1] - self.warehouse_coords[1]) ** 2
        )
        delivery_time = distance * 30 + 60 + 60
        print(f"Курьер {self.name} доставляет заказ {order.id}. Время: {delivery_time / 60:.2f} минут.")
        time.sleep(delivery_time)
        print(f"Курьер {self.name} доставил заказ {order.id}.")
        self.is_available = True
