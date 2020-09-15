# -*-coding:Utf-8 -*

# Standard library
import sys

# Third parties
import pygame as pg

# Local application/library specific
from .maze import Maze


class Engine():
    def __init__(self):
        pass

    def launch(self):
        maze = Maze()
        print(str(maze))

        while True:
            move = input() # TODO : Done with pygame
            maze.move_player(move)
            print(str(maze))

            if maze.game_is_done or move.lower() == 'quit':
                break

        print('Thanks for playing!')
        sys.exit()
