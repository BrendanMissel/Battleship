# Model class


class Model:
    @staticmethod
    def place_boat(board, ship):
        try:
            if Model.validate_loc(ship):
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
        try:
            if board.board[loc[0]][loc[1]] == 'O':
                board.board[loc[0]][loc[1]] = 'X'  # X represents a hit on a ship.
                board.score += 100

            elif board.board[loc[0]][loc[1]] == ' ':
                board.board[loc[0]][loc[1]] = '*'  # * represents a miss on the board.
                board.score -= 10

        except:
            print('Shot is invalid. Try again.')

    @staticmethod
    def validate_loc(ship):
        if ship.orientation == 'v':
            if ship.head[0] + ship.size > 9:
                return False
            else:
                return True
        elif ship.orientation == 'h':
            if ship.head[1] + ship.size > 9:
                return False
            else:
                return True
