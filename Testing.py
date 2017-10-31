# Test file for unit tests

import unittest
from Model import Model
# from View import View
from Board import Board
from Ship import Ship


class BattleshipTest(unittest.TestCase):
    @staticmethod
    def testBoardInit():
        test_object = Board()

        # test the size of the Board object
        expected_value = 10
        actual_value = test_object.size
        assert(actual_value == expected_value)

        # test that the board is empty
        expected_value = ' '

        for row in test_object.board:
            for x in row:
                if x != ' ':
                    actual_value = ''
                    break
                else:
                    actual_value = ' '
        assert(actual_value == expected_value)

    @staticmethod
    def testPlaceBoat():
        test_object = Board()
        m = Model()

        # test that a boat of size 1 will be placed at location (3,4) vertically
        expected_value = 'O'
        ship = Ship(1, (3, 4), 'v')
        m.place_boat(test_object, ship)
        actual_value = test_object.board[3][4]
        assert(actual_value == expected_value)

        # test that a boat of size 4 will be placed at location (3,4) horizontally
        expected_value = 'O'
        ship = Ship(4, (3, 4), 'h')
        m.place_boat(test_object, ship)
        actual_value = test_object.board[7][4]
        assert(actual_value == expected_value)

if __name__ == '__main__':
    b = BattleshipTest()
    b.testBoardInit()
    b.testPlaceBoat()
