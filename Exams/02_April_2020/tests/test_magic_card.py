from unittest import TestCase, main

from project.card.magic_card import MagicCard


class TestMagicCard(TestCase):
    def setUp(self) -> None:
        self.card = MagicCard('Magic Card')

    def test_attr_are_sett(self):
        self.assertEqual('Magic Card', self.card.name)
        self.assertEqual(5, self.card.damage_points)
        self.assertEqual(80, self.card.health_points)

    def test_card_name_with_empty_str_expect_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.card.name = ''
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_card_damage_points_with_negative_expect_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.card.damage_points = -1

        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))

    def test_health_points_with_negative_expect_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.card.health_points = -50
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))


if __name__ == '__main__':
    main()