from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal('Roro', 'dog', 'woolf')

    def test_attr_are_sett(self):
        self.assertEqual('Roro', self.mammal.name)
        self.assertEqual('dog', self.mammal.type)
        self.assertEqual('woolf', self.mammal.sound)

    def test_kingdom_initial(self):
        result = self.mammal._Mammal__kingdom
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_mammal_right_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual('Roro makes woolf', result)

    def test_return_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_get_info(self):
        result = self.mammal.info()
        self.assertEqual('Roro is of type dog', result)


if __name__ == '__main__':
    main()