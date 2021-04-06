from unittest import TestCase

from exam_prep.python_oop_exam_preparation_2_april_2020.project.battle_field import BattleField
from exam_prep.python_oop_exam_preparation_2_april_2020.project.card import MagicCard
from exam_prep.python_oop_exam_preparation_2_april_2020.project.card import TrapCard
from exam_prep.python_oop_exam_preparation_2_april_2020.project.player.advanced import Advanced
from exam_prep.python_oop_exam_preparation_2_april_2020.project.player.beginner import Beginner



class TestBattleField(TestCase):
    def test_battle_field_fight_when_attacker_is_dead(self):
        attacker = Beginner('Thor')
        enemy = Advanced('Hulk')
        battlefield = BattleField()
        card = MagicCard('magic card test')
        attacker.card_repository.add(card)
        card_1 = TrapCard('trap card test')
        enemy.card_repository.add(card_1)
        card_2 = TrapCard('trap card test_2')
        enemy.card_repository.add(card_2)
        card_3 = MagicCard('magic card test_3')
        enemy.card_repository.add(card_3)
        with self.assertRaises(ValueError) as context:
            battlefield.fight(attacker, enemy)
        self.assertEqual("Player's health bonus cannot be less than zero.", str(context.exception))

    def test_battle_field_when_player_is_dead(self):
        attacker = Beginner('Thor')
        enemy = Advanced('Hulk')
        battlefield = BattleField()
        with self.assertRaises(ValueError) as context:
            attacker.health = 0
            battlefield.fight(attacker, enemy)
        self.assertEqual('Player is dead!', str(context.exception))

