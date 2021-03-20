import pygame as pg
from constants import configs


class Clock():
    def __init__(self):
        self.clock = pg.time.Clock()

    def tick(self):
        self.clock.tick(configs.max_fps)
