class Topping:
    def __init__(self, topping_type, weight):
        self.weight = weight
        self.topping_type = topping_type

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        self.__topping_type = value

