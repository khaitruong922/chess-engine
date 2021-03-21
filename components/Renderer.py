import pygame as pg

from models.BoardState import BoardState
from models.ChessEngine import ChessEngine
from constants import resolution, colors
from constants.sprites import sprites
from constants.resolution import sq_size


def get_rect(c, r):
    return pg.Rect(c * sq_size, r * sq_size, sq_size, sq_size)


def get_square_surface(color, alpha):
    s = pg.Surface((sq_size, sq_size))
    s.set_alpha(alpha)
    s.fill(color)
    return s


def get_alpha_surface():
    s = pg.Surface((resolution.width, resolution.height), pg.SRCALPHA)
    return s


class Renderer:
    def __init__(self, chess_engine: ChessEngine, board_state: BoardState):
        self.chess_engine = chess_engine
        self.board_state = board_state
        self.screen = pg.display.set_mode((resolution.width, resolution.height))
        self.screen.fill(pg.Color(colors.white))

    def render(self):
        self.render_board()
        self.render_selected_square()
        self.render_checked_square()
        self.render_pieces()
        self.render_selected_piece_valid_moves()
        pg.display.flip()

    def render_board(self):
        def get_square_color(square_number: int):
            return colors.light_green if square_number % 2 == 0 else colors.green

        for r in range(8):
            for c in range(8):
                color = get_square_color(r + c)
                pg.draw.rect(self.screen, color, get_rect(c, r))
        pass

    def render_pieces(self):
        for r in range(8):
            for c in range(8):
                piece = self.chess_engine.board[r][c]
                if piece is None:
                    continue
                self.screen.blit(sprites[piece.get_name()], get_rect(c, r))
        pass

    def render_selected_square(self):
        square = self.board_state.selected_square
        if square is None:
            return
        r, c = square
        s = get_square_surface(colors.yellow, 100)
        self.screen.blit(s, (c * sq_size, r * sq_size))

    def render_selected_piece_valid_moves(self):
        s = get_alpha_surface()
        for move in self.board_state.get_selected_piece_valid_moves():
            r, c = move.end
            pg.draw.circle(s, colors.semi_trans_black, ((c + 0.5) * sq_size, (r + 0.5) * sq_size),
                           resolution.valid_move_indicator_radius)
        self.screen.blit(s, (0, 0))

    def render_checked_square(self):
        square = self.chess_engine.get_checked_square()
        print(square)
        if square is None:
            return
        r, c = square
        s = get_square_surface(colors.red, 100)
        self.screen.blit(s, (c * sq_size, r * sq_size))
