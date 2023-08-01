class Coffee:
    def __init__(self, name):
        self.name = name
        self._order = []
        self._customer = []

    def get_coffee_name(self):
        return self._name
    def set_coffee_name(self, name):
        if name and isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception
        
    name = property(get_coffee_name, set_coffee_name)
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._order.append(new_order)
        return self._order

    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer and isinstance(new_customer, Customer) and new_customer not in self._customer:
            self._customer.append(new_customer)
        return self._customer

    
    def num_orders(self):
        return len(self._order)
    
    def average_price(self):
        prices = [price.price for price in self._order]
        return sum(prices) / len(self._order)