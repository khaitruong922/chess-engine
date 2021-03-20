from models.Board import Board


class Move:
    def __init__(self, start, end, board: Board):
        self.start = start
        self.end = end
        self.board = board
        self.piece_moved = board.data[start[0]][start[1]]
        self.piece_captured = board.data[end[0]][end[1]]
