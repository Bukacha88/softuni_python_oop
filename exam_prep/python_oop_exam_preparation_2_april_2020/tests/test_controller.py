from unittest import TestCase


from exam_prep.python_oop_exam_preparation_2_april_2020.project import Controller


class TestController(TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_controller__init__(self):
        self.assertEqual('PlayerRepository', self.controller.player_repository.__class__.__name__)
        self.assertEqual('CardRepository', self.controller.card_repository.__class__.__name__)

    def test_controller__add_player_when_beginner(self):
        result = self.controller.add_player('Beginner', 'test username')
        msg = 'Successfully added player of type Beginner with username: test username'
        self.assertEqual(msg, result)

    def test_controller__add_player_when_advanced(self):
        result = self.controller.add_player('Advanced', 'test username')
        msg = 'Successfully added player of type Advanced with username: test username'
        self.assertEqual(msg, result)

    def test_controller__add_card__when_magic_card(self):
        result = self.controller.add_card('Magic', 'test name')
        msg = 'Successfully added card of type MagicCard with name: test name'
        self.assertEqual(msg, result)

    def test_controller__add_card__when_trap_card(self):
        result = self.controller.add_card('Trap', 'test name')
        msg = 'Successfully added card of type TrapCard with name: test name'
        self.assertEqual(msg, result)

    def test_controller__add_player_card(self):
        self.controller.add_player('Advanced', 'test username')
        self.controller.add_card('Trap', 'test name')
        result = self.controller.add_player_card('test username', 'test name')
        msg = 'Successfully added card: test name to user: test username'
        self.assertEqual(msg, result)

    def test_controller__fight(self):
        self.controller.add_player('Advanced', 'attacker username')
        self.controller.add_player('Beginner', 'enemy username')
        result = self.controller.fight('attacker username', 'enemy username')
        msg = 'Attack user health 250 - Enemy user health 90'
        self.assertEqual(msg, result)

    def test_controller__report(self):
        self.controller.add_player('Advanced', 'test username')
        self.controller.add_card('Trap', 'test name')
        self.controller.add_player_card('test username', 'test name')
        result = self.controller.report()
        msg = f'Username: test username - Health: 250 - Cards 1\n### Card: test name - Damage: 120\n'
        self.assertEqual(msg, result)

