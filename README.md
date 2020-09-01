# macgython

Help our hero to get out from the maze

## Getting Started

### Installing

If you just want to play the game, download [macgython.exe](macgython.exe). Note that it will only work on Windows OS.

If you want to modify the project, import the full repository. I built this project using Python 3.8.x and pygame 1.9.6. Just use this command to install the right requirements:
```bash
pip install -r requirements.txt
```

### Launching

Just double-click on the executable for a quick play.

If you downloaded the repository and the dependencies are installed, you can also launch the program with this:
```bash
python main.py
```

## Mission

This small program is a part of a application developer training.

### Mandatory features

To validate the project, I had to implement these features:
> - There is only one level. The structure (start, location of the walls, - finish), must be saved in a file to easily modify it if necessary.
> - MacGyver will be controlled by the directional keys of the keyboard.
> - The objects will be distributed randomly in the maze and - will change location if the user closes the game and relaunches it.
> - The game window will be a square that can display 15 sprites in length.
> - MacGyver will therefore have to move from square to square, with 15 squares along the length of the window!
> - He will recover an object simply by moving over it.
> - The program stops only if MacGyver has successfully retrieved all the objects and found the way out of the labyrinth. If he does not have all the objects - and he comes before the guard, he dies (life is cruel for the heroes).
> - The program will be standalone, that is to say that it can be executed on any computer.

### Constraints

I also had to respect some constraints
> - Use Git and Github,
> - Follow the best practices of PEP 8 and develop in a virtual environment using Python 3,
> - Code must be written in English: name of variables, comments, functions ...

In this part, I will detail how I created *macgython* for the sake of 

## My creation process

(Work in progress)

### Ideas for this part

Making the programm as a stand-alone: https://www.py2exe.org/

### Files Description

(Work in progress)

### Possible Improvements (TODO)

- Create tests
- Handle different levels
- Add music
- Use better sprites

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details