class Order:
    def __init__(self, customer, items, id):
        self.customer = customer
        self.items = items
        self.id = id
        self.status = "Created"
