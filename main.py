# -*-coding:Utf-8 -*

# Standard library
import os

# Third parties
import pygame as pg

# Local application/library specific
import settings
from mechanics import Maze


def main():
    """Launch the program."""
    maze = Maze.load_from_file(settings.LEVEL_PATH)
    print(str(maze))


if __name__ == "__main__":
    main()
