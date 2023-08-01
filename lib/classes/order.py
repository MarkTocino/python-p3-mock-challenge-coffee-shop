
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        coffee.orders(self)
        coffee.customers(customer)
        customer.orders(self)
        customer.coffees(coffee)

        Order.all.append(self)
    def get_order_price(self):
        return self._price
    def set_order_price(self, price):
        if price and isinstance (price, int) and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception
    price = property(get_order_price, set_order_price)

    def get_order_customer(self):
        return self._customer
    
    def set_order_customer(self, customer):
        from classes.customer import Customer
        if customer and isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception
    order_customer = property(get_order_customer, set_order_customer)

    def get_order_coffee(self):
        self._coffee
    def set_order_coffee(self, coffee):
        from classes.coffee import Coffee
        if coffee and isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception
    order_coffee= property(get_order_coffee,set_order_coffee)
