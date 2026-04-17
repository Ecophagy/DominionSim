from models.board import Board


class Simulator:
    def __init__(self, board: Board):
        self.board = board
        self.runs = 0

    def reset(self):
        self.board = Board()

    def run(self):
        self.reset()
        self.runs += 1

    def log_result(self):
        raise NotImplementedError