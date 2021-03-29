from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('Hulk', 10, 100, 50)
        self.enemy_hero = Hero('Thor', 6, 150, 70)

    def test_hero__init__expect_initialized(self):
        self.assertEqual('Hulk', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_hero_battle_when_fighting_himself_expect_exception(self):
        with self.assertRaises(Exception) as context:
            enemy_hero = self.hero
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_hero_battle_when_hero_health_is_0_expect_exception(self):

        with self.assertRaises(ValueError) as context:
            self.hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle_when_hero_health_is_negative_expect_exception(self):

        with self.assertRaises(ValueError) as context:
            self.hero.health = -10
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle_when_enemy_hero_health_is_0_expect_exception(self):

        with self.assertRaises(ValueError) as context:
            self.enemy_hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Thor. He needs to rest", str(context.exception))

    def test_hero_battle_when_enemy_hero_health_is_negative_expect_exception(self):

        with self.assertRaises(ValueError) as context:
            self.enemy_hero.health = -10
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Thor. He needs to rest", str(context.exception))

    def test_hero_battle_when_draw_health_both_negative(self):
        self.assertEqual('Draw', self.hero.battle(self.enemy_hero))

    def test_hero_battle_when_draw_health_both_0(self):
        self.enemy_hero.health = 500
        self.hero.health = 420
        self.assertEqual('Draw', self.hero.battle(self.enemy_hero))

    def test_hero_battle_when_you_win_enemy_hero_health_is_negative(self):
        self.hero.health = 600
        self.assertEqual('You win', self.hero.battle(self.enemy_hero))

    def test_hero_battle_when_you_win_enemy_hero_health_is_0(self):
        self.hero.health = 600
        self.enemy_hero.health = 500
        self.assertEqual('You win', self.hero.battle(self.enemy_hero))

    def test_hero_battle_when_you_lose_when_your_health_is_negative(self):
        self.enemy_hero.health = 700
        self.assertEqual('You lose', self.hero.battle(self.enemy_hero))

    def test_hero_battle_when_you_lose_when_your_health_is_0(self):
        self.enemy_hero.health = 700
        self.hero.health = 420
        self.assertEqual('You lose', self.hero.battle(self.enemy_hero))
        self.assertEqual(205, self.enemy_hero.health)
        self.assertEqual(7, self.enemy_hero.level)
        self.assertEqual(75, self.enemy_hero.damage)

    def test_hero__str__msg(self):
        self.assertEqual("Hero Hulk: 10 lvl\nHealth: 100\nDamage: 50\n", str(self.hero))
        self.hero.health = 600
        self.hero.battle(self.enemy_hero)
        self.assertEqual("Hero Hulk: 11 lvl\nHealth: 185\nDamage: 55\n", str(self.hero))


if __name__ == '__main__':
    main()
