from unittest import TestCase, main

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(TestCase):
    def setUp(self) -> None:
        self.player_repository = PlayerRepository()

    def test_attr_are_sett(self):
        self.assertEqual(0, self.player_repository.count)
        self.assertEqual([], self.player_repository.players)

    def test_add_non_existing_player_expect_add_it(self):
        player = Beginner('Beginner')
        self.player_repository.add(player)

        self.assertEqual(1, self.player_repository.count)
        self.assertEqual([player], self.player_repository.players)

    def test_add_player_with_existing_player_expect_raise(self):
        player = Beginner('Beginner')
        self.player_repository.add(player)

        with self.assertRaises(ValueError) as ex:
            self.player_repository.add(player)
        self.assertEqual('Player Beginner already exists!', str(ex.exception))

    def test_remove_player_with_empty_string_expect_raise(self):
        player = ''
        with self.assertRaises(ValueError) as ex:
            self.player_repository.remove(player)

        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

    def test_remove_with_existing_player_expect_remove_it(self):
        player = Beginner('Beginner')
        self.player_repository.add(player)

        self.player_repository.remove('Beginner')

        self.assertEqual(0, self.player_repository.count)
        self.assertEqual([], self.player_repository.players)

    def test_find_method(self):
        player = Beginner('Beginner')
        self.player_repository.add(player)
        result = self.player_repository.find('Beginner')
        self.assertEqual(player, result)


if __name__ == '__main__':
    main()