from exam_prep.exam_10_april_2021.project import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name=name, species=species, size=5, price=price)

    def eat(self):
        self.size += 2