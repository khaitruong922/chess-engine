class Move:
    def __init__(self, start, end, board):
        self.start = start
        self.end = end
        self.piece_moved = board[start[0]][start[1]]
        self.piece_captured = board[end[0]][end[1]]

    def __eq__(self, other):
        if not isinstance(other, Move):
            return False
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return str(self.start) + str(self.end)

    def __repr__(self):
        return str(self.start) + str(self.end)
