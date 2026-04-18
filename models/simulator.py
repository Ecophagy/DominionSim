from abc import ABC, abstractmethod
from models.board import Board


class Simulator(ABC):
    @abstractmethod
    def __init__(self, board: Board):
        self.board = board
        self.runs = 0

    def reset(self):
        self.board = Board()

    @abstractmethod
    def run(self):
        self.reset()
        self.runs += 1

    @abstractmethod
    def log_result(self):
        raise NotImplementedError