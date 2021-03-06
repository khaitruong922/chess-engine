from models.ChessEngine import ChessEngine
from models.Move import Move


class BoardState():
    def __init__(self, chess_engine: ChessEngine):
        self.chess_engine = chess_engine
        self.move_made = False
        self.selected_square = None
        self.clicks = []

    def select_square(self, r, c):
        # Handle first click
        if self.selected_square is None:
            # Return if the player select empty square or opponent pieces
            piece = self.chess_engine.get_piece(r, c)
            if piece is None or piece.is_white != self.chess_engine.is_white_turn:
                return
        if self.selected_square == (r, c):
            self.reset_click_state()
            return
        self.selected_square = r, c
        self.clicks.append(self.selected_square)
        if len(self.clicks) == 2:
            piece = self.chess_engine.get_piece(*self.clicks[1])
            if piece is not None and piece.is_white == self.chess_engine.is_white_turn:
                self.clicks.pop(0)
                return

            for move in self.chess_engine.valid_moves:
                if move.start == self.clicks[0] and move.end == self.clicks[1]:
                    self.make_move(move)
            self.reset_click_state()

    def reset_click_state(self):
        self.selected_square = None
        self.clicks = []

    def make_move(self, move):
        self.chess_engine.make_move(move)
        self.move_made = True
        self.chess_engine.calculate_valid_moves()
        self.chess_engine.calculate_player_state()

    def undo(self):
        self.chess_engine.undo_move()
        self.move_made = True
        self.chess_engine.calculate_valid_moves()
        self.chess_engine.calculate_player_state()

    def get_selected_piece_valid_moves(self):
        moves = []
        if self.selected_square is None:
            return moves
        return [move for move in self.chess_engine.valid_moves if move.start == self.selected_square]

    def handle_move_made(self):
        if not self.move_made:
            return
        last_player = "Black" if self.chess_engine.is_white_turn else "White"
        self.move_made = False
        if self.chess_engine.is_stalemated:
            print(f"{last_player} stalemate")
            return
        if self.chess_engine.is_checkmated:
            print(f"{last_player} checkmate")
            return
