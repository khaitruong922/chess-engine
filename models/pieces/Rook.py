from models.Move import Move
from models.Piece import Piece


class Rook(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def get_name(self):
        return self.get_color() + 'R'

    def get_possible_moves(self, r, c, board):
        moves = []
        # Up
        for des_r in range(r - 1, -1, -1):
            piece = board[des_r][c]
            start = r, c
            end = des_r, c
            if piece is None:
                moves.append(Move(start, end, board))
                continue
            if self.has_same_color(piece):
                break
            if not self.has_same_color(piece):
                moves.append(Move(start, end, board))
                break
        # Down
        for des_r in range(r + 1, 8, 1):
            piece = board[des_r][c]
            start = r, c
            end = des_r, c
            if piece is None:
                moves.append(Move(start, end, board))
                continue
            if self.has_same_color(piece):
                break
            if not self.has_same_color(piece):
                moves.append(Move(start, end, board))
                break
        # Right
        for des_c in range(c + 1, 8, 1):
            piece = board[r][des_c]
            start = r, c
            end = r, des_c
            if piece is None:
                moves.append(Move(start, end, board))
                continue
            if self.has_same_color(piece):
                break
            if not self.has_same_color(piece):
                moves.append(Move(start, end, board))
                break
        # Left
        for des_c in range(c - 1, -1, -1):
            piece = board[r][des_c]
            start = r, c
            end = r, des_c
            if piece is None:
                moves.append(Move(start, end, board))
                continue
            if self.has_same_color(piece):
                break
            if not self.has_same_color(piece):
                moves.append(Move(start, end, board))
                break

        return moves
