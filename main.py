from models.board import Board
from simulators.first_shuffle_collision import FirstShuffleCollisions
from simulators.opening_hands import OpeningHands


def main():
    board = Board()
    sim = FirstShuffleCollisions(board)
    runs = 100000

    for i in range(runs):
        sim.run()

    sim.log_result()

if __name__ == "__main__":
    main()
