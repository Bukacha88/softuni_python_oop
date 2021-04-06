from exam_prep.python_oop_exam_preparation_2_april_2020.project.card import Card


class MagicCard(Card):

    def __init__(self, name):
        super().__init__(name,  damage_points=5, health_points=80)