from .item import Item


class Provider:
    def __init__(self, name):
        """
        Создает поставщика с именем и доступным инвентарем.

        :param name: str - имя поставщика
        :param inventory: dict - словарь с товарами и их количеством
        """
        self.name = name
        self.inventory = {}
        self.itemsCounter = 0

    def addItem(self, item: Item):
        self.inventory[self.itemsCounter].append(item)
        item.provider_id = self.itemsCounter
        self.itemsCounter += 1

    def deliver(self, product, quantity):
        """
        Поставляет товар.

        :param product: str - название товара
        :param quantity: int - запрашиваемое количество
        :return: int - количество, которое удалось поставить
        """
        available_quantity = self.inventory.get(product, 0)
        delivered_quantity = min(available_quantity, quantity)
        self.inventory[product] = available_quantity - delivered_quantity
        print(f"{self.name} поставляет {delivered_quantity} единиц товара '{product}'.")
        return delivered_quantity
