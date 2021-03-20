from models.Piece import *
from models.Move import Move


class King(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def get_name(self):
        return self.get_color() + 'K'

    def get_possible_moves(self, r, c, board):
        moves = []
        king_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for delta_r, delta_c in king_moves:
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
