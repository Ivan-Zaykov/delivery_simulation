from classes.store import Store
from classes.storekeeper import Storekeeper
from classes.courier import Courier
from classes.order import Order
from classes.provider import Provider
from classes.item import Item

item = Item(name="Example Item", cost_price=50.0)

# Инициализация поставщиков
provider = Provider("Example поставщик")
provider.addItem(item)

# Инициализация склада
store = Store()

# Добавляем поставщиков склада
store.registerProvider(provider)

# Заказываем товары
store.requestProductsFromProviders("яблоки", 60)
print("Склад после заказа яблок:", store.stock)
print("Остатки у поставщиков:", provider1.inventory, provider2.inventory)

store.requestProductsFromProviders("бананы", 30)
print("Склад после заказа бананов:", store.stock)
print("Остатки у поставщиков:", provider1.inventory, provider2.inventory)

# Добавляем товары на склад
store.add_stock("яблоки", 10)
print("Склад после добавления яблок:", store.stock)
store.add_stock("бананы", 10)
print("Склад после добавления бананов:", store.stock)

# Инициализация работников
storekeeper1 = Storekeeper("Кладовщик 1")
courier1 = Courier("Курьер 1")

store.workers.append(storekeeper1)
store.workers.append(courier1)

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
