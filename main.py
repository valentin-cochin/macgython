# -*-coding:Utf-8 -*

# Standard library
import os

# Third parties
import pygame as pg

# Local application/library specific
from classes.maze import Maze


def main():
    """Launch the program."""
    maze = Maze()
    print(str(maze))
    maze.make_move()
    print(str(maze))


if __name__ == "__main__":
    main()
