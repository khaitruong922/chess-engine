import pygame as pg

from constants.resolution import sq_size
from models.ChessEngine import ChessEngine
from components.Renderer import Renderer
from components.Clock import Clock
from models.Move import Move


def main():
    pg.init()
    clock = Clock()
    chess_engine = ChessEngine()
    renderer = Renderer(chess_engine)
    is_playing = True
    selected_square = ()
    player_clicks = []
    while is_playing:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                is_playing = False
                continue
            if e.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                c = location[0] // sq_size
                r = location[1] // sq_size
                if selected_square == (r, c):
                    selected_square = ()
                    player_clicks.clear()
                else:
                    selected_square = r, c
                    player_clicks.append(selected_square)
                if len(player_clicks) == 2:
                    chess_engine.make_move(Move(player_clicks[0], player_clicks[1], chess_engine.board))
                    selected_square = ()
                    player_clicks.clear()
                print(selected_square)
                continue
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_z:
                    chess_engine.undo_move()
                    continue
                continue
        clock.tick()
        renderer.render()


if __name__ == '__main__':
    main()
