# -*-coding:Utf-8 -*
# Standard library
import os

# Local application/library specific
import settings


class Maze():

    # TODO: handle wrong files
    def __init__(self, name, layout):
        self.name = name
        self.layout = layout
        self._max_x, self._max_y = max(layout)

    def __repr__(self):
        return f'Maze({self.name}, {self.layout})'

    def __str__(self):
        char_list = []
        for y in range(self._max_y + 1):
            for x in range(self._max_x + 1):
                char = self.layout[x, y]
                char_list.append(char)
            char_list.append('\n')
        return ''.join(char_list)

    def update(self):
        pass

    @classmethod
    def load_from_file(self, path):
        file_name = path
        maze_name = file_name[:-3].lower()

        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        # Create a dictionary  with a tuple (x, y) for
        x = 0
        y = 0
        maze_layout = {}

        for line in content.splitlines():
            for char in line:
                maze_layout[x, y] = char
                x += 1
            x = 0
            y += 1

        return Maze(maze_name, maze_layout)


class Guardian():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def move(self, direction):
        pass


class Item():
    def __init__(self, name, position):
        pass
