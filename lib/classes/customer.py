class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._coffees = []
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        if name and isinstance (name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception
    name = property(get_name, set_name)

        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
        pass
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee and isinstance(new_coffee, Coffee) and new_coffee not in self._coffees:
            self._coffees.append(new_coffee)
        return self._coffees