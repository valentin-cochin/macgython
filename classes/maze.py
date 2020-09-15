# -*-coding:Utf-8 -*
# Standard library
import os
import random

# Local application/library specific
from .guardian import Guardian
from .item import Item
from .player import Player
from .settings import (EMPTY_TILE, GUARDIAN_TILE, ITEM_TILES, LEVEL_PATH,
                       MAC_TILE, WALL_TILE)


class Maze():

    directions = {
        'up': (0, -1),
        'right': (1, 0),
        'down': (0, 1),
        'left': (-1, 0)
    }

    def __init__(self, grid={}):
        self.grid = grid
        self.empty_paths = []
        self.player = None
        self.guardian = None
        self.items = []
        self.game_is_done = False

        self.set_grid_from_file()
        self.put_items_on_grid()

        self._max_x, self._max_y = max(self.grid)

    def __repr__(self):
        return f'Maze({self.grid})'

    def __str__(self):
        char_list = []
        for y in range(self._max_y + 1):
            for x in range(self._max_x + 1):
                char = self.grid[x, y]
                char_list.append(char)
            char_list.append('\n')
        return ''.join(char_list)

    def move_player(self, move):
        if Maze.directions.get(move) != False:
            old_position = (self.player.x, self.player.y)
            mv_x, mv_y = Maze.directions[move]
            dest_position = (self.player.x + mv_x, self.player.y + mv_y)

            if dest_position in self.empty_paths:
                if self.grid[dest_position] in ITEM_TILES:
                    self.player.bag.append(self.grid[dest_position])

                self.grid[old_position] = EMPTY_TILE
                self.grid[dest_position] = MAC_TILE

            elif self.grid[dest_position] == GUARDIAN_TILE:
                self.player.alive = False

    def set_grid_from_file(self):
        """Set grid, player, guardian and empty_paths using a txt file."""
        with open(LEVEL_PATH, "r", encoding="utf-8") as file:
            content = file.read()

        x = 0
        y = 0

        for line in content.splitlines():
            for char in line:
                self.grid[x, y] = char
                if char == EMPTY_TILE:
                    self.empty_paths.append((x, y))
                elif char == MAC_TILE:
                    self.player = Player(x, y)
                elif char == GUARDIAN_TILE:
                    self.guardian = Guardian(x, y)
                x += 1
            x = 0
            y += 1


    def put_items_on_grid(self):
        already_taken_position = []

        for char in ITEM_TILES:
            # utiliser boucle while
            x, y = random.choice(self.empty_paths)
            if (x, y) not in already_taken_position:
                already_taken_position.append((x, y))
                self.grid[x, y] = char
                self.items.append((x, y))
