from models.Move import Move
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
        self.valid_moves = []
        self.is_checked = False
        self.is_checkmated = False
        self.is_stalemated = False
        self.white_king_location = (7, 4)
        self.black_king_location = (0, 4)
        self.calculate_valid_moves()

    def get_piece(self, r, c):
        return self.board[r][c]

    def make_move(self, move, should_do_castle_move=True):
        self.board[move.start[0]][move.start[1]] = None
        self.board[move.end[0]][move.end[1]] = move.piece_moved
        move.piece_moved.move_count += 1
        if move.is_pawn_promotion:
            self.board[move.end[0]][move.end[1]] = Queen(move.piece_moved.is_white)
        elif isinstance(move.piece_moved, King):
            if move.piece_moved.is_white:
                self.white_king_location = move.end
            else:
                self.black_king_location = move.end
        if move.is_castle_move and should_do_castle_move:
            end = move.end
            if end == (7, 2):
                rook = self.get_piece(7, 0)
                self.board[7][3] = rook
                self.board[7][0] = None
            elif end == (7, 6):
                rook = self.get_piece(7, 7)
                self.board[7][5] = rook
                self.board[7][7] = None
            elif end == (0, 2):
                rook = self.get_piece(0, 0)
                self.board[0][3] = rook
                self.board[0][0] = None
            elif end == (0, 6):
                rook = self.get_piece(0, 7)
                self.board[0][5] = rook
                self.board[0][7] = None
        self.moves.append(move)
        self.switch_turn()

    def undo_move(self, should_do_castle_move=True):
        if len(self.moves) == 0:
            return
        move = self.moves.pop()
        self.board[move.start[0]][move.start[1]] = move.piece_moved
        move.piece_moved.move_count -= 1
        self.board[move.end[0]][move.end[1]] = move.piece_captured
        if isinstance(move.piece_moved, King):
            if move.piece_moved.is_white:
                self.white_king_location = move.start
            else:
                self.black_king_location = move.start
        if move.is_castle_move and should_do_castle_move:
            end = move.end
            if end == (7, 2):
                rook = self.get_piece(7, 3)
                self.board[7][0] = rook
                self.board[7][3] = None
            elif end == (7, 6):
                rook = self.get_piece(7, 5)
                self.board[7][7] = rook
                self.board[7][5] = None
            elif end == (0, 2):
                rook = self.get_piece(0, 3)
                self.board[0][0] = rook
                self.board[0][3] = None
            elif end == (0, 6):
                rook = self.get_piece(0, 5)
                self.board[0][7] = rook
                self.board[0][5] = None
        self.switch_turn()

    def _is_checked(self):
        self.switch_turn()
        for move in self.get_possible_moves():
            if isinstance(move.piece_captured, King):
                self.switch_turn()
                return True
        self.switch_turn()
        return False

    def calculate_valid_moves(self):
        self.valid_moves = self.get_valid_moves()
        print(self.valid_moves)

    def calculate_player_state(self):
        self.is_checked = self._is_checked()
        self.is_stalemated = not self.is_checked and len(self.valid_moves) == 0
        self.is_checkmated = self.is_checked and len(self.valid_moves) == 0

    def get_checked_square(self):
        if self.is_checked:
            return self.white_king_location if self.is_white_turn else self.black_king_location
        return None

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
            if move.is_castle_move and self.is_checked:
                continue
            self.make_move(move, should_do_castle_move=False)  # Make the move so now it is opponent turn
            # Check if you are not being checked after making the move
            self.switch_turn()  # Back to your turn
            self.calculate_player_state()
            if not self.is_checked:
                valid_moves.append(move)
            self.switch_turn()  # Pass turn back to opponent
            self.undo_move(should_do_castle_move=False)  # Undo so it is your turn now
        return valid_moves

    def switch_turn(self):
        self.is_white_turn = not self.is_white_turn
