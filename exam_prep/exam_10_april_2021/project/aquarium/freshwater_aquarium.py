from exam_prep.exam_10_april_2021.project import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name=name, capacity=50)