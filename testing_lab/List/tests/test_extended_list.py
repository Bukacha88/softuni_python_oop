from testing_lab.List.extendet_list.extended_list import IntegerList

from unittest import TestCase,main


class TestIntegerList(TestCase):
    def test_integer_list_add__when_int__expect_add_it(self):
        integer_list = IntegerList()
        internal_list = integer_list.add(1)
        self.assertEqual([1], internal_list)

    def test_integer_list_add__when_str__expect_exception(self):
        integer_list = IntegerList()
        with self.assertRaises(ValueError):
            integer_list.add('as')

    def test_integer_list_remove_index__when_valid_index__expect_to_remove_and_return_it(self):
        value_to_be_removed = 3
        integer_list = IntegerList(1, 2, value_to_be_removed, 4)
        result = integer_list.remove_index(2)
        self.assertEqual(value_to_be_removed, result)
        self.assertEqual([1, 2, 4], integer_list.get_data())

    def test_integer_list_remove_index__when_invalid_negative_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = -4
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)

    def test_integer_list_remove_index__when_invalid_positive_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 3
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)

    def test_integer_list_init__when_only_integers__expect_to_create_it(self):
        IntegerList(1, 2, 3)

    def test_integer_list_init__when_not_only_integers__expect_to_create_it(self):
        with self.assertRaises(Exception):
            IntegerList(1, 2, "as")

    def test_integer_list_get__when_valid_index__expect_to_remove_and_return_it(self):
        value_to_be_shown = 3
        integer_list = IntegerList(1, 2, value_to_be_shown, 4)
        result = integer_list.get(2)
        self.assertEqual(value_to_be_shown, result)

    def test_integer_list_get__when_invalid_negative_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = -4
        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_integer_list_get__when_invalid_positive_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 3
        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_integer_insert__when_valid_index_and_value__expect_to_insert_it(self):
        integer_list = IntegerList(1, 2, 3)
        index = 1
        value = 4
        integer_list.insert(index, value)

    def test_integer_insert__when_invalid_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 6
        value = 4
        with self.assertRaises(IndexError) as ex:
            integer_list.insert(index, value)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_integer_insert__when_value_is_str__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 1
        value = "as"
        with self.assertRaises(ValueError) as ex:
            integer_list.insert(index, value)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_integer_list_get_biggest__expect_to_return_biggest(self):
        biggest_num = 17
        integer_list = IntegerList(1, 3, biggest_num, 4, 6)
        actual = integer_list.get_biggest()
        self.assertEqual(biggest_num, actual)

    def test_integer_list_get_index__when_value_in_the_list__expect_return_index(self):
        integer_list = IntegerList(1, 2, 3, 4)
        value = 2
        result = integer_list.get_index(value)
        self.assertEqual(1, result)

    def test_integer_list_get_index__when_value_not_in_the_list__expect_return_index(self):
        integer_list = IntegerList(1, 2, 3, 4)
        value = 5
        with self.assertRaises(Exception):
            integer_list.get_index(value)


if __name__ == '__main__':
    main()