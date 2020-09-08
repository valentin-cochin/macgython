# -*-coding:Utf-8 -*

# Standard library
import sys

# Local application/library specific
from .settings import (EMPTY_TILE, GUARDIAN_TILE, ITEM_TILES, MAC_TILE,
                       WALL_TILE)


class Player():
    directions = {
        'up': (0, -1),
        'right': (1, 0),
        'down': (0, 1),
        'left': (-1, 0)
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.bag = []

    def enter_move(self, maze_grid, empty_paths):
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()
        elif Player.directions.get(move) != False:
            old_position = (self.x, self.y)
            mv_x, mv_y = Player.directions[move]
            dest_position = (self.x + mv_x, self.y + mv_y)

            if dest_position in empty_paths:
                if maze_grid[dest_position] in ITEM_TILES:
                    self.bag.append(maze_grid[dest_position])

                maze_grid[old_position] = EMPTY_TILE
                maze_grid[dest_position] = MAC_TILE

            elif maze_grid[dest_position] == GUARDIAN_TILE:
                self.alive = False

    def is_legit_move(self, grid, move):
        # -> vérifier s'il y a un objet ou non sur la case de destination
        # -> "ramasser" cet objet. redéfinir la valeur de la clé dans la grille à "chemin"
        # -> ajouter l'objet ramassé dans le sac a dos de MacGyver
        pass
