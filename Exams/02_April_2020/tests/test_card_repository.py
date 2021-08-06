from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(TestCase):
    def setUp(self) -> None:
        self.card_repository = CardRepository()

    def test_init(self):
        self.assertEqual(0, self.card_repository.count)
        self.assertEqual([], self.card_repository.cards)

    def test_add_non_existing_card_expect_add_it(self):
        card = MagicCard('MagicCard')
        self.card_repository.add(card)

        self.assertEqual(1, self.card_repository.count)
        self.assertEqual([card], self.card_repository.cards)

    def test_add_card_with_existing_card_expect_raise(self):
        card = MagicCard('MagicCard')
        self.card_repository.add(card)

        with self.assertRaises(ValueError) as ex:
            self.card_repository.add(card)
        self.assertEqual('Card MagicCard already exists!', str(ex.exception))

    def test_remove_card_with_empty_string_expect_raise(self):
        card = ''
        with self.assertRaises(ValueError) as ex:
            self.card_repository.remove(card)

        self.assertEqual("Card cannot be an empty string!", str(ex.exception))

    def test_remove_with_existing_card_expect_remove_it(self):
        card = MagicCard('MagicCard')
        self.card_repository.add(card)
        self.card_repository.remove('MagicCard')

        self.assertEqual(0, self.card_repository.count)
        self.assertEqual([], self.card_repository.cards)

    def test_find_method(self):
        card = MagicCard('MagicCard')
        self.card_repository.add(card)
        result =self.card_repository.find('MagicCard')
        self.assertEqual(card, result)


if __name__ == '__main__':
    main()