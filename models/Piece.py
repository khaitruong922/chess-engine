class Piece:
    def __init__(self, is_white):
        self.is_white = is_white

    def get_color(self):
        return 'W' if self.is_white else 'B'

    def get_name(self):
        raise NotImplementedError("Please specify the name for this piece")

    def get_possible_moves(self, r, c, board):
        raise NotImplementedError("Please specify the possible moves for this piece")

    def has_same_color(self, piece):
        if not isinstance(piece, Piece):
            return False
        return self.is_white == piece.is_white
