# -*-coding:Utf-8 -*

# Local application/library specific
from .settings import (EMPTY_TILE, GUARDIAN_TILE, ITEM_TILES, MAC_TILE,
                       WALL_TILE)


class Hero():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.bag = []
