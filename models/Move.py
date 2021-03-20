from models.ChessEngine import ChessEngine


class Move:
    def __init__(self, start, end, board):
        self.start = start
        self.end = end
        self.piece_moved = board[start[0]][start[1]]
        self.piece_captured = board[end[0]][end[1]]
