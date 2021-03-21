from models.pieces.Bishop import Bishop
from models.pieces.King import King
from models.pieces.Knight import Knight
from models.pieces.Pawn import Pawn
from models.pieces.Queen import Queen
from models.pieces.Rook import Rook


class ChessEngine:
    def __init__(self):
        self.board = [
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
        self.board[move.start[0]][move.start[1]] = None
        self.board[move.end[0]][move.end[1]] = move.piece_moved
        self.moves.append(move)
        self.switch_turn()

    def undo_move(self):
        if len(self.moves) == 0:
            return
        move = self.moves.pop()
        self.board[move.start[0]][move.start[1]] = move.piece_moved
        self.board[move.end[0]][move.end[1]] = move.piece_captured
        self.switch_turn()

    def is_checking(self):
        for move in self.get_possible_moves():
            if isinstance(move.piece_captured, King):
                return True
        return False

    def is_checked(self):
        self.switch_turn()
        for move in self.get_possible_moves():
            if isinstance(move.piece_captured, King):
                self.switch_turn()
                return True
        self.switch_turn()
        return False

    def has_no_valid_moves(self):
        return True if len(self.get_valid_moves()) == 0 else False

    def is_stalemated(self):
        return not self.is_checked() and self.has_no_valid_moves()

    def is_checkmated(self):
        return self.is_checked() and self.has_no_valid_moves()

    def get_checked_square(self):
        square = None
        self.switch_turn()
        for move in self.get_possible_moves():
            if isinstance(move.piece_captured, King):
                square = move.end[0], move.end[1]
        self.switch_turn()
        return square

    def get_possible_moves(self):
        moves = []
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece is None:
                    continue
                if (self.is_white_turn and piece.is_white) or (not self.is_white_turn and not piece.is_white):
                    moves.extend(piece.get_possible_moves(r, c, self.board))
        return moves

    def get_valid_moves(self):
        possible_moves = self.get_possible_moves()
        valid_moves = []
        for move in possible_moves:
            self.make_move(move)
            # Now it's opponent turn
            if not self.is_checking():
                valid_moves.append(move)
            self.undo_move()
        return valid_moves

    def switch_turn(self):
        self.is_white_turn = not self.is_white_turn
