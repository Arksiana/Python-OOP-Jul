# from unittest import TestCase, main
#
# from project.hero import Hero
#
#
# class TestHero(TestCase):
#     def setUp(self):
#         self.hero = Hero('Hero', 5, 100, 10)
#         self.enemy = Hero('Enemy', 10, 80, 20)
#
#     def test_attr_are_sett(self):
#         self.assertEqual('Hero', self.hero.username)
#         self.assertEqual(5, self.hero.level)
#         self.assertEqual(100, self.hero.health)
#         self.assertEqual(10, self.hero.damage)
#
#     def test_battle_when_enemy_name_equal_to_self_name_raise(self):
#         self.enemy_name = Hero('Hero', 1, 100, 50)
#         with self.assertRaises(Exception) as ex:
#             self.hero.battle(self.enemy_name)
#         self.assertEqual("You cannot fight yourself", str(ex.exception))
#
#     def test_enemy_health_below_zero_expect_raise(self):
#         self.enemy.health = -10
#         with self.assertRaises(Exception) as ex:
#             self.hero.battle(self.enemy)
#         self.assertEqual("You cannot fight Enemy. He needs to rest", str(ex.exception))
#
#     def test_hero_and_enemy_health_below_zero_expect_msg(self):
#         self.enemy.health = 50
#         result = self.hero.battle(self.enemy)
#         self.assertEqual('Draw', result)
#
#     def test_hero_wins(self):
#         self.hero.damage = 200
#         self.hero.health = 300
#         result = self.hero.battle(self.enemy)
#         self.assertEqual('You win', result)
#         self.assertEqual(6, self.hero.level)
#         self.assertEqual(105, self.hero.health)
#         self.assertEqual(105, self.hero.health)
#
#     def test_hero_lose(self):
#         self.enemy.damage = 200
#         self.enemy.health = 300
#         result = self.hero.battle(self.enemy)
#         self.assertEqual('You lose', result)
#         self.assertEqual(11, self.enemy.level)
#         self.assertEqual(255, self.enemy.health)
#         self.assertEqual(205, self.enemy.damage)
#
#     def test_battle_when_self_health_is_below_0_raises_value_error(self):
#         self.hero.health = -10
#         self.assertEqual(-10, self.hero.health)
#         with self.assertRaises(ValueError) as ex:
#             self.hero.battle(self.enemy)
#         self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))
#
#     def test_str_method(self):
#         result = f"Hero Hero: 5 lvl\n" \
#                f"Health: 100\n" \
#                f"Damage: 10\n"
#         actual = self.hero.__str__()
#         self.assertEqual(result, actual)
#
#
# if __name__ == '__main__':
#     main()


from unittest import TestCase
from project.hero import Hero

class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Harry", 100, 200, 300)
        self.enemy = Hero("Ron", 100, 200, 300)
        self.strong_hero = Hero("Strong Harry", 10000, 20000, 30000)

    def test_init(self):
        hero = Hero("Harry", 10, 100, 20)
        self.assertEqual("Harry", hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(20, hero.damage)

    def test_battle_with_one_self(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_no_health(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_no_health(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Ron. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        res = self.hero.battle(self.enemy)
        self.assertEqual("Draw", res)

    def test_battle_win(self):
        resu = self.strong_hero.battle(self.enemy)
        self.assertEqual("You win", resu)

    def test_battle_lose(self):
        res = self.hero.battle(self.strong_hero)
        self.assertEqual("You lose", res)