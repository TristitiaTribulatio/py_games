import pygame as pg

from settings import *


class Ball:
    def __init__(self):
        self.rect = pg.Rect(BALL["dx"], BALL["dy"], BALL["size"], BALL["size"])
        self.dir = "top-left"

    def move(self):
        self.rect.x += DIRECTIONS[self.dir][0] * BALL["speed"]
        self.rect.y += DIRECTIONS[self.dir][1] * BALL["speed"]