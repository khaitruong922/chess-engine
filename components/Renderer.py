import pygame as pg

from models.BoardState import BoardState
from models.ChessEngine import ChessEngine
from constants import resolution, colors
from constants.sprites import sprites
from constants.resolution import sq_size


def get_rect(c, r):
    return pg.Rect(c * sq_size, r * sq_size, sq_size, sq_size)


class Renderer:
    def __init__(self, chess_engine: ChessEngine, board_state: BoardState):
        self.chess_engine = chess_engine
        self.board_state = board_state
        self.screen = pg.display.set_mode((resolution.width, resolution.height))
        self.screen.fill(pg.Color(colors.white))

    def render(self):
        self.render_board()
        self.render_selected_square()
        self.render_pieces()
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
        if self.board_state.selected_square == ():
            return
        r, c = self.board_state.selected_square
        s = pg.Surface((sq_size, sq_size))
        s.set_alpha(100)
        s.fill(colors.blue)
        self.screen.blit(s, (c * sq_size, r * sq_size))
