class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, type, sound):
        self.sound = sound
        self.type = type
        self.name = name

    @staticmethod
    def get_kingdom():
        return Mammal.__kingdom

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def info(self):
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())