from models.Piece import *


class Bishop(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def get_name(self):
        return self.get_color() + 'B'

    def get_possible_moves(self, r, c, board):
        moves = []
        return moves
