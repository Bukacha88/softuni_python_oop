from exam_prep.python_oop_exam_preparation_2_april_2020.project.player.player import Player


class Beginner(Player):
    def __init__(self, username):
        super().__init__(username, health=50)