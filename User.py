# User class

from Board import Board


class User:
    def __init__(self, usnm):
        self.username = usnm
        self.board = Board()
        self.board_used = False
