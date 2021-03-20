from models.Piece import *
from models.Move import Move


class Knight(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def get_name(self):
        return self.get_color() + 'N'

    def get_possible_moves(self, r, c, board):
        moves = []
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for delta_r, delta_c in knight_moves:
            des_r = r + delta_r
            des_c = c + delta_c
            if not is_in_board(des_r) or not is_in_board(des_c):
                break
            piece = board[des_r][des_c]
            start = r, c
            end = des_r, des_c
            if self.has_same_color(piece):
                continue
            moves.append(Move(start, end, board))
        return moves
