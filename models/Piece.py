class Piece:
    def __init__(self, is_white):
        self.is_white = is_white

    def get_color(self):
        return 'W' if self.is_white else 'B'

    def get_name(self):
        raise NotImplementedError("Please specify the name for this piece")

    def get_valid_move(self, board):
        raise NotImplementedError("Please specify the valid moves for this piece")
