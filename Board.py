# Board class


class Board:
    def __init__(self):
        self.size = 10  # The board size for both the x and y direction
        self.board = [[' ' for i in range(0, self.size)] for i in range(0, self.size)]  # The board is a 2D list of
        # blank values.
        self.score = 0
