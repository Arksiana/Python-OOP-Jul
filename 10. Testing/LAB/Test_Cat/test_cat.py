from unittest import TestCase, main

from Test_Cat.cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat('Cat')

    def test_attr_are_sett(self):
        self.assertEqual('Cat', self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_eat_when_already_fed_expect_raise(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as exc:
            self.cat.eat()
        self.assertEqual('Already fed.', str(exc.exception))

    def test_cat_eat_when_is_not_fed(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)
        self.assertEqual(True, self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_cat_sleep_when_not_fed_expect_raise(self):
        with self.assertRaises(Exception) as exc:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(exc.exception))

    def test_cat_sleep_when_fed(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == '__main__':
    main()