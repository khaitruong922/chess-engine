class Move:
    def __init__(self, start, end, board, is_enpassant_move=False, is_castle_move=False):
        self.start = start
        self.end = end
        self.piece_moved = board[start[0]][start[1]]
        self.piece_captured = board[end[0]][end[1]]
        self.is_pawn_promotion = self.piece_moved.get_type() == "P" and (
                (self.piece_moved.is_white and self.end[0] == 0) or (
                not self.piece_moved.is_white and self.end[0] == 7))
        self.is_enpassant_move = is_enpassant_move
        self.is_castle_move = is_castle_move

    def __eq__(self, other):
        if not isinstance(other, Move):
            return False
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return str(self.start) + str(self.end)

    def __repr__(self):
        return str(self.start) + str(self.end)
