from models.Piece import *
from models.Move import Move


class Pawn(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def get_type(self):
        return 'P'

    def get_possible_moves(self, r, c, board):
        moves = []
        diagonals = []
        if self.is_white:
            if is_in_board(r - 1) and board[r - 1][c] is None:
                moves.append(Move((r, c), (r - 1, c), board))
                # 2 step advance
                if r == 6 and board[r - 2][c] is None:
                    moves.append(Move((r, c), (r - 2, c), board))
            diagonals.extend([(-1, -1), (-1, 1)])
        else:
            if is_in_board(r + 1) and board[r + 1][c] is None:
                moves.append(Move((r, c), (r + 1, c), board))
                # 2 step advance
                if r == 1 and board[r + 2][c] is None:
                    moves.append(Move((r, c), (r + 2, c), board))
            diagonals.extend([(1, -1), (1, 1)])
        for delta_r, delta_c in diagonals:
            des_r = r + delta_r
            des_c = c + delta_c
            if not is_in_board(des_r) or not is_in_board(des_c):
                continue
            piece = board[des_r][des_c]
            start = r, c
            end = des_r, des_c
            if piece is None:
                continue
            if self.has_same_color(piece):
                continue
            moves.append(Move(start, end, board))
        return moves
