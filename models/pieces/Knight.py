from models.Piece import *


class Knight(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    def get_type(self):
        return 'N'

    def get_possible_moves(self, r, c, board):
        return self.get_positional_moves(self.knight_moves, r, c, board)
