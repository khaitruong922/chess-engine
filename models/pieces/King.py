from models.Piece import *
from models.pieces.Rook import Rook


class King(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.king_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def get_type(self):
        return 'K'

    def get_castle_moves(self, r, c, board):
        moves = []
        queen_side_empty = all(board[r][i] is None for i in range(1, 4))
        king_side_empty = all(board[r][i] is None for i in range(5, 7))
        if queen_side_empty:
            piece = board[r][0]
            if isinstance(piece, Rook) and not piece.has_moved():
                moves.append(Move((r, 4), (r, 2), board, is_castle_move=True))
        if king_side_empty:
            piece = board[r][7]
            if isinstance(piece, Rook) and not piece.has_moved():
                moves.append(Move((r, 4), (r, 6), board, is_castle_move=True))
        return moves

    def get_possible_moves(self, r, c, board):
        moves = []
        moves.extend(self.get_positional_moves(self.king_moves, r, c, board))
        if self.has_moved():
            return moves
        if self.is_white:
            moves.extend(self.get_castle_moves(7, c, board))
        else:
            moves.extend(self.get_castle_moves(0, c, board))
        return moves
