from loguru import logger

from models.board import Board
from models.card import Card
from models.simulator import Simulator


class FirstShuffleBuyingPower(Simulator):
    def __init__(self, board: Board):
        super().__init__(board)
        self.buying_power = {}

    def run(self):
        self.board.draw(5)
        self.board.gain(Card("Silver", 2))
        self.board.discard()
        self.board.draw(5)
        self.board.discard()
        self.board.gain(Card("Silver", 2))
        self.board.draw(5)

        buying_power = 0
        for card in self.board.hand:
            buying_power = buying_power + card.value
        if buying_power in self.buying_power.keys():
            self.buying_power[buying_power] += 1
        else:
            self.buying_power[buying_power] = 1

    def log_result(self):
        logger.info(f"Hand 3 buying power after buying 2 silver")
        buying_power = dict(sorted(self.buying_power.items()))
        for k, v in buying_power.items():
            logger.info(f"Buying power {k}: {v / self.runs * 100:.2f}%")