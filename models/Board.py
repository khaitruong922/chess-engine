from constants.pieces import *
from constants import resolution
from models.pieces.Bishop import Bishop
from models.pieces.King import King
from models.pieces.Knight import Knight
from models.pieces.Pawn import Pawn
from models.pieces.Queen import Queen
from models.pieces.Rook import Rook


class Board:
    def __init__(self):
        self.data = [
            [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), Knight(False),
             Rook(False)],
            [Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True)],
            [Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True), Rook(True)],
        ]
        self.moves = []
        self.is_white_turn = True

    def make_move(self, move):
        self.data[move.start[0]][move.start[1]] = None
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

    def get_possible_moves(self):
        for r in range(resolution.dimension):
            for c in range(resolution.dimension):
                piece = self.data[r][c]
                if piece == OO:
                    continue
                pass
        return []

    def get_valid_moves(self):
        return self.get_possible_moves()
