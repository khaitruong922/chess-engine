from models.Piece import *


class Rook(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def get_type(self):
        return 'R'

    def get_possible_moves(self, r, c, board):
        return self.get_directional_moves(self.directions, r, c, board)
