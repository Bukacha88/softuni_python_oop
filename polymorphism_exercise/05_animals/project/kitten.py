from exam_prep.python_oop_exam_16_aug_2020.project import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Female')

    def make_sound(self):
        return "Meow"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old Female {self.__class__.__name__}"
