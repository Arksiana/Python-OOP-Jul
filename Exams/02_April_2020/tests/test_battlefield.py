from unittest import TestCase, main

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(TestCase):
    def setUp(self) -> None:
        self.battle_field = BattleField()
        self.attacker = Advanced('Advanced')
        self.enemy = Beginner('Beginner')

    def test_increase_beginner_attr(self):
        self.battle_field.fight(self.attacker, self.enemy)
        self.assertEqual(50 + 40, self.enemy.health)

    def test_increase_damage_points_bonus(self):
        card = MagicCard('Magic Card')
        self.attacker.card_repository.add(card)

        self.battle_field.fight(self.attacker, self.enemy)

        self.assertEqual(250 + 80, self.attacker.health)
        self.assertEqual(85, self.enemy.health)

    def test_fight_when_one_is_dead_expect_raise(self):
        self.attacker.health = 0
        with self.assertRaises(ValueError) as context:
            self.battle_field.fight(self.attacker, self.enemy)

        self.assertEqual('Player is dead!', str(context.exception))
if __name__ == '__main__':
    main()