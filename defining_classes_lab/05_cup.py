class Cup:
    def __init__(self, size, quantity):
        self.quantity = quantity
        self.size = size

    def fill(self, milliliters):
        if self.size >= self.quantity + milliliters:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(20)
cup.fill(10)
print(cup.status())