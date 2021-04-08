import unittest

from exam_prep.python_oop_retake_exam_19_dec_2020.tests.project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory('test name', 10)

    def test_paint_factory__init(self):
        self.assertEqual('test name', self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)
        # self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertDictEqual({}, self.paint_factory.products)

    def test_paint_factory_add_ingredient_when_not_valid(self):
        msg = f"Ingredient of type purple not allowed in PaintFactory"
        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient('purple', 7)
        self.assertEqual(msg, str(context.exception))

    def test_paint_factory_add_ingredient_when_capacity_less_than_quantity(self):
        msg = "Not enough space in factory"
        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient('white', 12)
        self.assertEqual(msg, str(context.exception))

    def test_paint_factory_add_ingredient_when_not_in_ingredient_key_quantity_0(self):
        self.paint_factory.add_ingredient('white', 0)
        self.assertEqual({'white': 0}, self.paint_factory.ingredients)

    def test_paint_factory_add_ingredient_when_not_in_ingredient_key_quantity_4(self):
        self.paint_factory.add_ingredient('white', 4)
        self.assertEqual({'white': 4}, self.paint_factory.ingredients)

    def test_paint_factory_add_ingredient_when_in_ingredient_key(self):
        self.paint_factory.add_ingredient('white', 0)
        self.assertEqual({'white': 0}, self.paint_factory.ingredients)
        self.paint_factory.add_ingredient('white', 6)
        self.assertEqual({'white': 6}, self.paint_factory.ingredients)

    def test_paint_factory_remove_ingredient_when_not_in_ingredient_key(self):

        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient('white', 3)
        self.assertEqual("No such ingredient in the factory", context.exception.args[0])

    def test_paint_factory_remove_ingredient_when_quantity_is_greater_than_actual(self):
        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient('white', 4)
            self.paint_factory.remove_ingredient('white', 6)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_paint_factory_remove_ingredient_when_successful(self):
        self.paint_factory.add_ingredient('white', 6)
        self.paint_factory.remove_ingredient('white', 4)
        self.assertEqual({'white': 2}, self.paint_factory.ingredients)

    def test_paint_factory_products(self):
        self.paint_factory.add_ingredient('white', 6)
        self.paint_factory.remove_ingredient('white', 4)
        self.assertEqual({'white': 2}, self.paint_factory.products)

    def test_paint_factory_can_add_true(self):
        self.paint_factory.add_ingredient('white', 2)
        self.paint_factory.add_ingredient('blue', 2)
        self.assertTrue(self.paint_factory.can_add(2))

    def test_paint_factory_all_methods(self):
        self.paint_factory.add_ingredient('white', 2)
        self.paint_factory.add_ingredient('blue', 1)
        self.paint_factory.add_ingredient('green', 1)
        self.paint_factory.add_ingredient('yellow', 1)
        self.paint_factory.add_ingredient('red', 1)
        self.assertEqual(5, len(self.paint_factory.ingredients.keys()))

    def test_paint_factory_can_add_false(self):
        self.paint_factory.add_ingredient('white', 2)
        self.paint_factory.add_ingredient('blue', 2)
        self.assertFalse(self.paint_factory.can_add(10))

    def test__repr__method(self):
        self.paint_factory.add_ingredient('green', 6)
        result = self.paint_factory.__repr__()
        expected = "Factory name: test name with capacity 10.\ngreen: 6\n"
        self.assertEqual(expected, result)