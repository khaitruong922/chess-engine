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
    move_made = False
    selected_square = ()
    player_clicks = []
    valid_moves = chess_engine.get_valid_moves()
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
                print(selected_square)
                if len(player_clicks) == 2:
                    move = Move(player_clicks[0], player_clicks[1], chess_engine.board)
                    print(valid_moves)
                    if move in valid_moves:
                        chess_engine.make_move(move)
                        move_made = True
                    selected_square = ()
                    player_clicks.clear()
                continue
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_z:
                    chess_engine.undo_move()
                    move_made = True
                    continue
                continue
        if move_made:
            valid_moves = chess_engine.get_valid_moves()
            move_made = False
        clock.tick()
        renderer.render()


if __name__ == '__main__':
    main()
