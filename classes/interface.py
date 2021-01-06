# -*-coding:Utf-8 -*

# Third parties
import pygame as pg


class Interface():
    def __init__(self):
        pass

    def display_frame(self, screen, maze_grid):
        pass

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
        done = False
        direction = None

        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN: # A key is pressed
                if event.key == pg.K_UP:
                    direction = 'up'
                elif event.key == pg.K_RIGHT:
                    direction = 'right'
                elif event.key == pg.K_DOWN:
                    direction = 'down'
                elif event.key == pg.K_LEFT:
                    direction = 'left'
        return done, direction

# Pas utiliser  cette classe
class Block(pg.sprite.Sprite):
    """ This class represents a simple block the player collects. """
    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pg.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 1

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()
