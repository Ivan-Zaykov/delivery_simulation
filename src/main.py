

from classes.store import Store
from classes.storekeeper import Storekeeper
from classes.courier import Courier
from classes.order import Order
from classes.customer import Customer
from src.classes.supplier import Supplier
from src.utils.constants import Constants
from src.utils.virtual_time import GlobalVirtualTime

# Инициализация поставщиков
supplier = Supplier('Поставщик 1')

# Инициализация склада
store = Store('Склад 1')

# Необходимые товары
goods = {
    "Pizza": 10,
    "Soda": 20
}

# Поставщик доставляет товары на склад
supplier.deliver_goods(goods)

# Склад обновляет стоки
store.update_stocks(goods)

# Инициализируем и добавляем работников (кладовщика и курьера) на склад
storekeeper1 = Storekeeper("Сборщик 1")
storekeeper1.start_shift(4)

courier1 = Courier("Курьер 1")
courier1.start_shift(8)

store.workers.append(storekeeper1)
store.workers.append(courier1)

# Добавляем клиента и заказ
customer1 = Customer('Клиент 1', (60, 70))
order1 = Order(customer1, {"Pizza": 2, "Soda": 1})

# Склад обрабатывает заказ
store.process_order(order1)

# Продвигаем время вперёд
deltaMinutes = 600
GlobalVirtualTime.advance_time(deltaMinutes)
print(f"По прошествии {round(deltaMinutes / Constants.MINUTES_PER_HOUR)} часов...")

# Добавляем клиента и заказ
customer2 = Customer('Клиент 2', (80, 110))
order2 = Order(customer1, {"Pizza": 5, "Soda": 3})

# Склад обрабатывает заказ
store.process_order(order2)
