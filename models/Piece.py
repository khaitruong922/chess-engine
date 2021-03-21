from models.Move import Move


class Piece:
    def __init__(self, is_white):
        self.is_white = is_white

    def get_color(self):
        return 'W' if self.is_white else 'B'

    def get_type(self):
        raise NotImplementedError("Please specify the type for this piece")

    def get_name(self):
        return self.get_color() + self.get_type()

    def get_possible_moves(self, r, c, board):
        raise NotImplementedError("Please specify the possible moves for this piece")

    def has_same_color(self, piece):
        if not isinstance(piece, Piece):
            return False
        return self.is_white == piece.is_white

    def get_positional_moves(self, positions, r, c, board):
        moves = []
        for delta_r, delta_c in positions:
            des_r = r + delta_r
            des_c = c + delta_c
            if not is_in_board(des_r) or not is_in_board(des_c):
                continue
            piece = board[des_r][des_c]
            start = r, c
            end = des_r, des_c
            if self.has_same_color(piece):
                continue
            moves.append(Move(start, end, board))
        return moves

    def get_directional_moves(self, directions, r, c, board):
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
                moves.append(Move(start, end, board))
                break
        return moves


def is_in_board(x):
    return 0 <= x <= 7
