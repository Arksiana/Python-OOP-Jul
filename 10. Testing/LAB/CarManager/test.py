from unittest import TestCase, main

from CarManager.car_manager import Car


class TestCarManager(TestCase):
    def setUp(self):
        self.car = Car('Super', 'Mack', 1, 10)

    def test_attr_are_sett(self):
        self.assertEqual("Super", self.car.make)
        self.assertEqual('Mack', self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(10, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_empty_str_expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

if __name__ == '__main__':
    main()