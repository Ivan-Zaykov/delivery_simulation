from classes.store import Store
from classes.storekeeper import Storekeeper
from classes.courier import Courier
from classes.order import Order

# Инициализация склада и работников
# Инициализация склада и работников
store = Store()

storekeeper1 = Storekeeper("Сборщик 1")
courier1 = Courier("Курьер 1")

store.workers.append(storekeeper1)
store.workers.append(courier1)

# Добавляем сток на склад
store.add_stock("Pizza", 10)
store.add_stock("Soda", 20)

# Добавляем заказ
customer = type('Customer', (object,), {"address": (60, 70)})
order1 = Order(customer, {"Pizza": 2, "Soda": 1}, 1)
store.process_order(order1)

# Назначаем сборщика и курьера
store.assign_storekeeper(order1)
store.assign_courier(order1)

# Завершаем смену работников
storekeeper1.end_shift()
courier1.end_shift()
