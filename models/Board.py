from constants.pieces import *


class Board:
    def __init__(self):
        self.data = [
            [BR, BN, BB, BQ, BK, BB, BN, BR],
            [BP, BP, BP, BP, BP, BP, BP, BP],
            [OO, OO, OO, OO, OO, OO, OO, OO],
            [OO, OO, OO, OO, OO, OO, OO, OO],
            [OO, OO, OO, OO, OO, OO, OO, OO],
            [OO, OO, OO, OO, OO, OO, OO, OO],
            [WP, WP, WP, WP, WP, WP, WP, WP],
            [WR, WN, WB, WQ, WK, WB, WN, WR],
        ]
        self.moves = []
        self.is_white_turn = True

    def make_move(self, move):
        self.data[move.start[0]][move.start[1]] = OO
        self.data[move.end[0]][move.end[1]] = move.piece_moved
        self.moves.append(move)
        self.is_white_turn = not self.is_white_turn

    def undo_move(self):
        if len(self.moves) == 0:
            return
        move = self.moves.pop()
        self.data[move.start[0]][move.start[1]] = move.piece_moved
        self.data[move.end[0]][move.end[1]] = move.piece_captured
        self.is_white_turn = not self.is_white_turn
