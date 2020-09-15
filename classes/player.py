# -*-coding:Utf-8 -*

# Standard library
import sys

# Local application/library specific
from .settings import (EMPTY_TILE, GUARDIAN_TILE, ITEM_TILES, MAC_TILE,
                       WALL_TILE)


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.bag = []
