class Item:
    def __init__(self, name: str, cost_price: float):
        """
        Инициализация товара
        :param name: Название товара
        :param cost_price: Себестоимость товара
        """
        self.name = name
        self.cost_price = cost_price

    @property
    def store_id(self):
        return self.store_id

    @store_id.setter
    def store_id(self, new_value: int):
        self.store_id = new_value

    @property
    def provider_id(self):
        """Геттер для value."""
        return self.store_id

    @provider_id.setter
    def provider_id(self, new_value: int):
        """Сеттер для value."""
        self.provider_id = new_value

    def __repr__(self):
        """Возвращает строковое представление объекта."""
        return (
            f"Item(store_id={self.store_id}, provider_id={self.provider_id}, "
            f"name='{self.name}', cost_price={self.cost_price})"
        )
