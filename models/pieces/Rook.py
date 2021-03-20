from models.Piece import *
from models.Move import Move


class Rook(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def get_name(self):
        return self.get_color() + 'R'

    def get_possible_moves(self, r, c, board):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        moves = []
        for d in directions:
            for i in range(1, 8):
                des_r = r + d[0] * i
                des_c = c + d[1] * i
                if not is_in_board(des_r) or not is_in_board(des_c):
                    break
                piece = board[des_r][des_c]
                start = r, c
                end = des_r, des_c
                if piece is None:
                    moves.append(Move(start, end, board))
                    continue
                if self.has_same_color(piece):
                    break
                if not self.has_same_color(piece):
                    moves.append(Move(start, end, board))
                    break

        return moves
