from models.card import Card
from random import shuffle

class Board:
    def __init__(self):
        self.deck = []
        self.deck.extend([Card("Copper", 1)] * 7)
        self.deck.extend([Card("Estate")] * 3)
        self._shuffle()

        self.discard_pile = []
        self.hand = []

    def draw(self, number=1):
        for i in range(number):
            if not self.deck:
                self.reshuffle()
                if not self.deck:
                    # Deck is empty
                    return
            self.hand.append(self.deck.pop())

    def discard(self):
        self.discard_pile.extend(self.hand)
        self.hand = []

    def _shuffle(self):
        shuffle(self.deck)

    def reshuffle(self):
        self.deck = self.discard_pile
        self._shuffle()
        self.discard_pile = []

    def gain(self, card:Card):
        self.discard_pile.append(card)