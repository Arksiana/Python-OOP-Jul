from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count: int = 0
        self.cards: list = []

    def add(self, card: Card):
        for c in self.cards:
            if c.name == card.name:
                raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")

        c_to_remove = self.find(card)
        self.cards.remove(c_to_remove)
        self.count -= 1

    def find(self, username: str):
        for c in self.cards:
            if c.name == username:
                return c
