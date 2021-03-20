from models.Piece import Piece


class Rook(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def get_name(self):
        return self.get_color() + 'R'

    def get_possible_moves(self, r, c, board):
        raise NotImplementedError("Please specify the possible moves for this piece")