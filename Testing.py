# Test file for unit tests

import unittest
from Model import Model
from View import View
from Board import Board
from Ship import Ship


class BattleshipTest(unittest.TestCase):
    def testBoardInit(self):
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

if __name__ == '__main__':
    b = BattleshipTest()
    b.testBoardInit()
