from models.ChessEngine import ChessEngine
from models.Move import Move


class BoardState():
    def __init__(self, chess_engine: ChessEngine):
        self.chess_engine = chess_engine
        self.move_made = False
        self.selected_square = ()
        self.clicks = []
        self.valid_moves = self.chess_engine.get_valid_moves()

    def select_square(self, r, c):
        if self.selected_square == (r, c):
            self.reset_click_state()
            return
        self.selected_square = r, c
        self.clicks.append(self.selected_square)
        if len(self.clicks) == 2:
            move = Move(self.clicks[0], self.clicks[1], self.chess_engine.board)
            if move in self.valid_moves:
                self.chess_engine.make_move(move)
                self.move_made = True
            self.reset_click_state()

    def reset_click_state(self):
        self.selected_square = ()
        self.clicks = []

    def undo(self):
        self.chess_engine.undo_move()
        self.move_made = True

    def get_selected_piece_valid_moves(self):
        moves = []
        if self.selected_square == ():
            return moves
        return [move for move in self.valid_moves if move.start == self.selected_square]

    def handle_move_made(self):
        if not self.move_made:
            return
        self.valid_moves = self.chess_engine.get_valid_moves()
        self.move_made = False
