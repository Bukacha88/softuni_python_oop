class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.toppings_capacity = toppings_capacity
        self.dough = dough
        self.name = name
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @property
    def topping_capacity(self):
        return self.__toppings_capacity

    @topping_capacity.setter
    def topping_capacity(self, value):
        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    def add_topping(self, topping):
        if topping.weight + sum([t for t in self.toppings.values()]) > self.topping_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        return sum([t for t in self.toppings.values()]) + self.dough.weight
