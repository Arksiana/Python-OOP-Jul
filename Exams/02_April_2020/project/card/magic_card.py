from project.card.card import Card


class MagicCard(Card):
    def __init__(self, name):
        super(MagicCard, self).__init__(name, 5, 80)
