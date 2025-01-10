from classes.store import Store
from classes.storekeeper import Storekeeper
from classes.courier import Courier
from classes.order import Order
from classes.customer import Customer
from src.classes.supplier import Supplier

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
courier1 = Courier("Курьер 1")
store.workers.append(storekeeper1)
store.workers.append(courier1)

# Добавляем клиента и заказ
customer1 = Customer('Клиент 1', (60, 70))
order1 = Order(customer1, {"Pizza": 2, "Soda": 1})
store.process_order(order1)

# Завершаем смену работников
storekeeper1.end_shift()
courier1.end_shift()
