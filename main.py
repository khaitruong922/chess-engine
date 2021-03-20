import pygame as pg

from models.Board import Board
from components.Renderer import Renderer
from components.Clock import Clock


def main():
    pg.init()
    clock = Clock()
    board = Board()
    renderer = Renderer(board)
    is_playing = True
    while is_playing:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                is_playing = False
        clock.tick()
        renderer.render()


if __name__ == '__main__':
    main()
