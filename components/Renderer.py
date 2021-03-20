import pygame as pg
from models.Board import Board
from constants import resolution, colors, pieces
from constants.sprites import sprites
from constants.resolution import sq_size


def get_rect(c, r):
    return pg.Rect(c * sq_size, r * sq_size, sq_size, sq_size)


class Renderer:
    def __init__(self, board: Board):
        self.board = board
        self.screen = pg.display.set_mode((resolution.width, resolution.height))
        self.screen.fill(pg.Color(colors.white))

    def render(self):
        self.render_board()
        self.render_pieces()
        pg.display.flip()

    def render_board(self):
        def get_square_color(square_number: int):
            return colors.light_green if square_number % 2 == 0 else colors.green

        for r in range(resolution.dimension):
            for c in range(resolution.dimension):
                color = get_square_color(r + c)
                pg.draw.rect(self.screen, color, get_rect(c, r))
        pass

    def render_pieces(self):
        for r in range(resolution.dimension):
            for c in range(resolution.dimension):
                piece = self.board.data[r][c]
                if piece == pieces.OO:
                    continue
                self.screen.blit(sprites[piece], get_rect(c, r))
        pass
