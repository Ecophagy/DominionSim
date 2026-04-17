from loguru import logger

from models.board import Board
from models.simulator import Simulator


class OpeningHands(Simulator):
    def __init__(self, board: Board):
        super().__init__(board)
        self.opening_hands = {}

    def run(self):
        super().run()
        self.board.draw(5)

        copper_count = len([c for c in self.board.hand if c.name == "Copper"])
        if copper_count in self.opening_hands:
            self.opening_hands[copper_count] += 1
        else:
            self.opening_hands[copper_count] = 1

    def log_result(self):
        logger.info(f"Odds of 4/3 vs 5/2 split in opening hands")
        five_two = self.opening_hands[5] + self.opening_hands[2]
        four_three = self.opening_hands[4] + self.opening_hands[3]

        logger.info(f"4/3: {four_three/self.runs * 100:.2f}%")
        logger.info(f"5/2: {five_two/self.runs * 100:.2f}%")

