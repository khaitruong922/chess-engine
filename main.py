import pygame as pg

from constants.resolution import sq_size
from models.BoardState import BoardState
from models.ChessEngine import ChessEngine
from components.Renderer import Renderer
from components.Clock import Clock


def main():
    pg.init()
    clock = Clock()
    chess_engine = ChessEngine()
    board_state = BoardState(chess_engine)
    renderer = Renderer(chess_engine, board_state)
    is_playing = True
    while is_playing:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                is_playing = False
                continue
            if e.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                r = location[1] // sq_size
                c = location[0] // sq_size
                board_state.select_square(r, c)
                continue
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_z:
                    board_state.undo()
                    continue
                if e.key == pg.K_r:
                    clock = Clock()
                    chess_engine = ChessEngine()
                    board_state = BoardState(chess_engine)
                    renderer = Renderer(chess_engine, board_state)
                    is_playing = True
                    continue
                continue
        board_state.handle_move_made()
        clock.tick()
        renderer.render()


if __name__ == '__main__':
    main()
