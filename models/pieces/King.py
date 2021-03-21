from models.Piece import *


class King(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.king_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def get_type(self):
        return 'K'

    def get_possible_moves(self, r, c, board):
        return self.get_positional_moves(self.king_moves, r, c, board)
