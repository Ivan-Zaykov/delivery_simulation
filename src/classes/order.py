class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self._id = None
        self.status = "Created"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if self._id is not None:
            raise ValueError("ID заказа уже назначен и не может быть изменён.")
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID должен быть положительным целым числом.")
        self._id = value

    def __str__(self):
        """Возвращает строковое представление объекта Order."""
        return f"`customer={self.customer.name}, items={self.items}`"
