from models.Piece import *


class Bishop(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def get_type(self):
        return 'B'

    def get_possible_moves(self, r, c, board):
        return self.get_directional_moves(self.directions, r, c, board)
