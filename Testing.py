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
        actual_value = 0

        assert(actual_value == expected_value)

        # test that the board is empty
        expected_value = ' '
        actual_value = ''
        assert(actual_value == expected_value)

if __name__ == '__main__':
    b = BattleshipTest()
    b.testBoardInit()
