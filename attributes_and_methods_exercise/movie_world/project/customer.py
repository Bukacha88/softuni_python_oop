class Customer:
    def __init__(self, name, age, id):
        self.id = id
        self.age = age
        self.name = name
        self.rented_dvds = []

    def __repr__(self):
        dvd_names = ", ".join(dvd.name for dvd in self.rented_dvds)
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's " \
               f"({dvd_names})"
