import pygame as pg
from constants.pieces import *
from constants.resolution import sq_size

sprites = {}

for piece in pieces:
    if piece == OO:
        continue
    sprites[piece] = pg.transform.scale(pg.image.load(f"assets/images/{piece}.png"),
                                        (sq_size, sq_size))
