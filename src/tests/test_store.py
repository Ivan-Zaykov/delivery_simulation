import unittest
from src.classes.store import Store
from src.classes.storekeeper import Storekeeper
from src.classes.courier import Courier
from src.classes.order import Order
from src.classes.customer import Customer


class TestStore(unittest.TestCase):
    def setUp(self):
        """Инициализация объектов для тестов."""                                   
        self.store = Store("Test Store")
        self.storekeeper = Storekeeper("Test Storekeeper")
        self.courier = Courier("Test Courier")
        self.store.workers.extend([self.storekeeper, self.courier])

    def test_update_stocks(self):
        """Тестирует обновление стоков."""
        goods = {"Pizza": 10, "Soda": 20}
        self.store.update_stocks(goods)
        self.assertEqual(self.store.stock["Pizza"], 10)
        self.assertEqual(self.store.stock["Soda"], 20)

        # Добавляем дополнительные стоки
        self.store.update_stocks({"Pizza": 5})
        self.assertEqual(self.store.stock["Pizza"], 15)

    def test_process_order_stock_reduction(self):
        """Тестирует обработку заказа и уменьшение стоков."""
        self.store.update_stocks({"Pizza": 10, "Soda": 5})

        self.storekeeper.start_shift(8)  # Запускаем смену для кладовщика
        self.courier.start_shift(8)  # Запускаем смену для курьера

        customer = Customer("Test Customer", (60, 70))
        order = Order(customer, {"Pizza": 3, "Soda": 2})
        self.store.process_order(order)

        self.assertEqual(self.store.stock["Pizza"], 7)
        self.assertEqual(self.store.stock["Soda"], 3)

    def test_order_id_assignment(self):
        """Тестирует назначение уникального id заказу."""

        self.storekeeper.start_shift(8)  # Запускаем смену для кладовщика
        self.courier.start_shift(8)  # Запускаем смену для курьера

        customer = Customer("Test Customer", (60, 70))
        order1 = Order(customer, {"Pizza": 3})
        self.store.process_order(order1)

        self.assertEqual(order1.id, 1)

        # Новый заказ
        order2 = Order(customer, {"Soda": 2})
        self.store.process_order(order2)
        self.assertEqual(order2.id, 2)

    def test_assign_storekeeper(self):
        """Тестирует назначение кладовщика на заказ."""
        self.storekeeper.start_shift(8)  # Запускаем смену для кладовщика
        customer = Customer("Test Customer", (60, 70))
        order = Order(customer, {"Pizza": 1})
        self.store.assign_order_id_and_items_count(order)
        storekeeper = self.store.assign_storekeeper(order)

        self.assertIsNotNone(storekeeper._current_order)
        self.assertEqual(storekeeper._current_order.id, order.id)

    def test_assign_courier(self):
        """Тестирует назначение курьера на доставку."""
        self.courier.start_shift(8)  # Запускаем смену для курьера
        customer = Customer("Test Customer", (60, 70))
        order = Order(customer, {"Pizza": 1})
        self.store.assign_order_id_and_items_count(order)
        courier = self.store.assign_courier(order)

        self.assertIsNotNone(courier._current_order)
        self.assertEqual(courier._current_order.id, order.id)

    def test_assign_order_id_and_items_count(self):
        goods = {"Pizza": 10}
        self.store.update_stocks(goods)

        customer = Customer("Test Customer", (60, 70))
        order1 = Order(customer, {"Pizza": 5})
        self.store.assign_order_id_and_items_count(order1)
        self.assertEqual(5, self.store.orders[order1.id].items['Pizza'])

        # На складе осталось 5, поэтому склад выдаст только 5, а не 7
        order2 = Order(customer, {"Pizza": 7})
        self.store.assign_order_id_and_items_count(order2)
        self.assertEqual(5, self.store.orders[order1.id].items['Pizza'])
