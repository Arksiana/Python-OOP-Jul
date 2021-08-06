from unittest import TestCase, main

from project.player.advanced import Advanced


class TestAdvanced(TestCase):
    def setUp(self) -> None:
        self.player = Advanced('TestName')

    def test_attr_are_sett(self):
        self.assertEqual("TestName", self.player.username)
        self.assertEqual(250, self.player.health)
        self.assertEqual('CardRepository', self.player.card_repository.__class__.__name__)

    def test_username_with_empty_str_expect_raise(self):
        username = ''
        with self.assertRaises(ValueError) as ex:
            Advanced(username)
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception),)

    def test_health_with_negative_value_expect_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.player.health = -1
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_is_dead_with_zero_value_expect_true(self):
        self.player.health = 0
        self.assertTrue(self.player.is_dead)

    def test_is_dead_with_positive_value_expect_False(self):
        self.assertFalse(self.player.is_dead)

    def test_take_damage_with_negative_value_expect_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.player.take_damage(-1)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))

    def test_take_damage_with_positive_value_expect_reduce_health(self):
        self.player.take_damage(50)
        self.assertEqual(200, self.player.health)
if __name__ == '__main__':
    main()