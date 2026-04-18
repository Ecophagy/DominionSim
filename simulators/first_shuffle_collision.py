from loguru import logger

from models.board import Board
from models.card import Card
from models.simulator import Simulator


class FirstShuffleCollisions(Simulator):
    def __init__(self, board: Board):
        super().__init__(board)
        self.hand_3_collisions = 0
        self.hand_4_collisions = 0

    def run(self):
        super().run()
        self.board.draw(5)
        self.board.gain(Card("A", 2))
        self.board.discard()
        self.board.draw(5)
        self.board.discard()
        self.board.gain(Card("B", 2))
        self.board.draw(5)

        matches = len(([c for c in self.board.hand if c.name == "A" or c.name == "B"]))
        if matches == 2:
            self.hand_3_collisions += 1

        self.board.discard()
        self.board.draw(5)

        matches = len(([c for c in self.board.hand if c.name == "A" or c.name == "B"]))
        if matches == 2:
            self.hand_4_collisions += 1

    def log_result(self):
        logger.info(f"Collisions in hand 3: {self.hand_3_collisions/self.runs * 100:.2f}%")
        logger.info(f"Collisions in hand 4: {self.hand_4_collisions/self.runs * 100:.2f}%")