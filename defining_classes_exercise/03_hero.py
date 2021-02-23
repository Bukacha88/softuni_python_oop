class Hero:
    def __init__(self, name, health):
        self.health = health
        self.name = name

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, heal_amount):
        self.health += heal_amount
        return self.health

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))