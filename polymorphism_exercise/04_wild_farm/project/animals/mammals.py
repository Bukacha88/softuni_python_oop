from exam_prep.python_oop_exam_16_aug_2020.project import Mammal
from exam_prep.python_oop_exam_16_aug_2020.project import Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Mouse.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Dog.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Meat) and not isinstance(food, Vegetable):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Cat.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_INCREASE = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Tiger.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity

