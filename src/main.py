from classes.warehouse import Warehouse
from classes.picker import Picker
from classes.courier import Courier
from classes.order import Order

# Инициализация склада и работников
# Инициализация склада и работников
warehouse = Warehouse()

picker1 = Picker("Сборщик 1")
courier1 = Courier("Курьер 1")

warehouse.workers.append(picker1)
warehouse.workers.append(courier1)

# Добавляем сток на склад
warehouse.add_stock("Pizza", 10)
warehouse.add_stock("Soda", 20)

# Добавляем заказ
customer = type('Customer', (object,), {"address": (60, 70)})
order1 = Order(customer, {"Pizza": 2, "Soda": 1}, 1)
warehouse.process_order(order1)

# Назначаем сборщика и курьера
warehouse.assign_picker(order1)
warehouse.assign_courier(order1)

# Завершаем смену работников
picker1.end_shift()
courier1.end_shift()