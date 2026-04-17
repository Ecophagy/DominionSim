from models.card import Card


class Deck:
    def __init__(self):
        self.deck = []
        self.deck.extend([Card("Copper")] * 7)
        self.deck.extend([Card("Estate")] * 3)

