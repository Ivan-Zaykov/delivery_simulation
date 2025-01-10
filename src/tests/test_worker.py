import unittest

from src.classes.courier import Courier
from src.classes.customer import Customer
from src.classes.order import Order
from src.classes.store import Store
from src.classes.storekeeper import Storekeeper
from src.utils.constants import Constants
from src.utils.virtual_time import GlobalVirtualTime


class TestWorker(unittest.TestCase):
    def setUp(self):
        """Инициализация объектов для тестов."""
        self.store = Store("Test Store")
        self.storekeeper = Storekeeper("Test Storekeeper")
        self.courier = Courier("Test Courier")
        self.store.workers.extend([self.storekeeper, self.courier])

    def test_worker_is_available_by_shift(self):
        shift_hours = 8

        self.storekeeper.start_shift(shift_hours)  # Запускаем смену для кладовщика
        self.courier.start_shift(shift_hours)  # Запускаем смену для курьера
        self.assertEqual(True, self.storekeeper.is_available())
        self.assertEqual(True, self.courier.is_available())

        # Прошло время на 1 час большее, чем смена
        GlobalVirtualTime.advance_time((shift_hours + 1) * Constants.MINUTES_PER_HOUR)

        self.assertEqual(False, self.storekeeper.is_available())
        self.assertEqual(False, self.courier.is_available())

    def test_storekeeper_is_not_available_by_order(self):
        shift_hours = 8

        self.storekeeper.start_shift(shift_hours)  # Запускаем смену для кладовщика
        self.courier.start_shift(shift_hours)  # Запускаем смену для курьера

        customer = Customer("Test Customer", (60, 70))
        order = Order(customer, {"Pizza": 1})
        self.store.assign_order_id_and_items_count(order)
        storekeeper = self.store.assign_storekeeper(order)
        courier = self.store.assign_courier(order)

        self.assertEqual(False, storekeeper.is_available())  # Сборщик на заказе
        self.assertEqual(False, courier.is_available())  # Курьер на заказе
