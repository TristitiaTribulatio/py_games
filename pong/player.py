import pygame as pg

from settings import *


class Player:
    def __init__(self, side: str):
        self.rect = pg.Rect(
            WIDTH - PLAYER["dx"] - PLAYER["width"] if side == 'right' else PLAYER["dx"],
            PLAYER["dy"],
            PLAYER["width"],
            PLAYER["height"]
        )
        self.dir = "top"
        self.side = side
        self.score = 0

    def move(self):
        self.rect.y += PLAYER["speed"] * (-1 if self.dir == "top" else 1)