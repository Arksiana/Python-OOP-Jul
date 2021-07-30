from unittest import TestCase, main

from List.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.my_list = IntegerList(1, 2, 3, 4)

    def test_add_when_not_int_expect_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.my_list.add('a')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_add_add_when_element_is_int_expect_add(self):
        result = self.my_list.add(5)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_get_info_expect_return_list(self):
        result = self.my_list.get_data()
        self.assertEqual([1, 2, 3, 4], result)

    def test_remove_index_when_out_of_range_expect_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.my_list.remove_index(7)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_when_is_valid_expect_remove_it(self):
        result = self.my_list.remove_index(0)
        self.assertEqual(1, result)

    def test_get_index_when_out_of_range_expect_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.my_list.get(7)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_index_with_valid_expect_return(self):
        result = self.my_list.get(0)
        self.assertEqual(1, result)

    def test_insert_when_out_of_range_expect_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.my_list.insert(7, 7)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_when_element_not_int_expect_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.my_list.insert(0, 'a')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_wit_valid_index_and_element(self):
        self.my_list.insert(3, 5)
        result = self.my_list.get_data()
        self.assertEqual([1, 2, 3, 5, 4], result)

    def test_get_biggest_expect_return(self):
        result = self.my_list.get_biggest()
        self.assertEqual(4, result)

    def test_get_index_expect_return(self):
        result = self.my_list.get_index(1)
        self.assertEqual(0, result)


if __name__ == '__main__':
    main()
