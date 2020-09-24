# -*-coding:Utf-8 -*

# Standard library
import sys

# Third parties
import pygame as pg

# Local application/library specific
from .interface import Interface
from .maze import Maze
from .settings import SCREEN_SIZE


class Engine():
    def __init__(self):
        pass

    def launch(self):
        """ Main program function."""
        maze = Maze()
        interface = Interface()

        # Initialize Pygame and set up the window
        pg.init()
        screen = pg.display.set_mode(SCREEN_SIZE)
        pg.display.set_caption("My Game")
        pg.mouse.set_visible(False)
        clock = pg.time.Clock()

        done = False

        while not done:
            done, move = interface.process_events()
            maze.run_logic(move)
            interface.display_frame(screen)
            clock.tick(60)  # Pause for the next frame

        # Close window and exit
        pg.quit()
        sys.exit()
