# model class


class Model:
    @staticmethod
    def place_boat(board, ship):
        try:
            if ship.orientation == 'v':
                for i in range(0, ship.size):
                    board.board[ship.head[0]+i][ship.head[1]] = 'O'
            elif ship.orientation == 'h':
                for i in range(0, ship.size):
                    board.board[ship.head[0]][ship.head[1]+i] = 'O'
        except:
            print('Boat is out of bounds. Try again.')

    @staticmethod
    def fire_shot(board, loc):
        pass
