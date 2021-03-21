from models.Piece import *
from models.Move import Move


class Pawn(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def get_type(self):
        return 'P'

    def get_possible_moves(self, r, c, board):
        moves = []
        return moves