from unittest import TestCase, main

from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestController(TestCase):
    def setUp(self) -> None:
        self.controller = Controller()

    def test_init(self):
        self.assertEqual('CardRepository', self.controller.card_repository.__class__.__name__)
        self.assertEqual('PlayerRepository', self.controller.player_repository.__class__.__name__)

    def test_add_player_beginner_expect_return_message(self):
        player = Beginner('Beginner')

        result = self.controller.add_player(player.__class__.__name__, player.username)

        self.assertEqual('Beginner', self.controller.player_repository.players[0].username)
        self.assertEqual('Beginner', self.controller.player_repository.players[0].__class__.__name__)
        self.assertEqual('Successfully added player of type Beginner with username: Beginner', result)

    def test_add_player_advanced_expect_return_message(self):
        player = Advanced("Advanced")
        result = self.controller.add_player(player.__class__.__name__, player.username)

        self.assertEqual('Advanced', self.controller.player_repository.players[0].username)
        self.assertEqual('Advanced', self.controller.player_repository.players[0].__class__.__name__)
        self.assertEqual('Successfully added player of type Advanced with username: Advanced', result)

    def test_add_magic_card_expect_return_message(self):
        card = MagicCard('Magic Card')
        result = self.controller.add_card(card.__class__.__name__, card.name)

        self.assertEqual('Successfully added card of type MagicCardCard with name: Magic Card', result)

    def test_add_trap_card_expect_return_message(self):
        card = TrapCard('Trap Card')
        result = self.controller.add_card(card.__class__.__name__, card.name)

        self.assertEqual('Successfully added card of type TrapCardCard with name: Trap Card', result)

    def test_add_player_card_expect_return_message(self):
        player = Beginner('Beginner')
        card = MagicCard('Magic Card')

        self.controller.player_repository.add(player)
        self.controller.card_repository.add(card)

        result = self.controller.add_player_card(player.username, card.name)
        self.assertEqual([card], player.card_repository.cards)
        self.assertEqual('Successfully added card: Magic Card to user: Beginner', result)

    def test_fight(self):
        attacker = Advanced('Advanced')
        enemy = Beginner('Beginner')
        self.controller.add_player(attacker.__class__.__name__, attacker.username)
        self.controller.add_player(enemy.__class__.__name__, enemy.username)

        result = self.controller.fight(attacker.username, enemy.username)
        self.assertEqual('Attack user health 250 - Enemy user health 90', result)

    def test_report(self):
        self.controller.add_player('Beginner', 'Beginner')
        self.controller.add_player('Advanced', 'Advanced')
        self.controller.add_card('Magic', 'Magic')
        self.controller.add_card('Trap', 'Trap')
        self.controller.add_player_card('Beginner', 'Magic')
        self.controller.add_player_card('Advanced', 'Trap')

        expected = f'Username: Beginner - Health: 50 - Cards 1\n' \
                   f'### Card: Magic - Damage: 5\n' \
                   f'Username: Advanced - Health: 250 - Cards 1\n' \
                   f'### Card: Trap - Damage: 120\n'

        actual = self.controller.report()

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()
