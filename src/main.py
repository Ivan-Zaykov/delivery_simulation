from classes.store import Store
from classes.storekeeper import Storekeeper
from classes.courier import Courier
from classes.order import Order
from classes.customer import Customer


# Инициализация поставщиков

# Инициализация склада
store = Store()

# Инициализируем и добавляем работников (кладовщика и курьера) на склад
storekeeper1 = Storekeeper("Сборщик 1")
courier1 = Courier("Курьер 1")
store.workers.append(storekeeper1)
store.workers.append(courier1)

# Добавляем сток на склад
store.add_stock("Pizza", 10)
store.add_stock("Soda", 20)

# Добавляем заказ
customer1 = Customer('Customer 1', {"address": (60, 70)})
order1 = Order(customer1, {"Pizza": 2, "Soda": 1}, 1)
store.process_order(order1)

# Назначаем сборщика и курьера
store.assign_storekeeper(order1)
store.assign_courier(order1)

# Завершаем смену работников
storekeeper1.end_shift()
courier1.end_shift()
