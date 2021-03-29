import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):

    name = 'Kudjo'
    mammal_type = 'dog'
    sound = 'woof woof'
    __kingdom = 'animals'

    def setUp(self):
        self.mammal = Mammal(self.name, self.mammal_type, self.sound)

    def test_mammal__init__expect_to_initialized(self):
        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.mammal_type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)

    def test_if_get_kingdom_method_is_private(self):
        self.assertEqual(self.__kingdom, self.mammal._Mammal__kingdom)

    def test_mammal_make_sound_expect_return_msg(self):
        self.assertEqual('Kudjo makes woof woof', self.mammal.make_sound())

    def test_mammal_get_kingdom_expect_return___kingdom(self):
        self.assertEqual(self.__kingdom, self.mammal.get_kingdom())

    def test_mammal_info_expect_msg(self):
        self.assertEqual('Kudjo is of type dog', self.mammal.info())


if __name__ == '__main__':
    unittest.main()
