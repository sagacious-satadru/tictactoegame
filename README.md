# Tic Tac Toe Game

This is a simple implementation of the classic Tic Tac Toe game using Pygame and Numpy libraries in Python.

## Installation

To use this game, you need to have Python 3 installed. You can download Python from the official website: https://www.python.org/downloads/

You also need to have Pygame and Numpy libraries installed. You can install them using pip, the package installer for Python. Open a terminal or command prompt and type:

```
pip install pygame
pip install numpy
```

## Usage

To run the game, simply open the terminal or command prompt, navigate to the directory where the `tictactoe.py` file is located, and type:

```
python tictactoe.py
```

The game window will open, and you can start playing by clicking on the squares on the board.

## How to Play

The game is played on a 3x3 board, with two players taking turns to place their marks (either O or X) on the board. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.

To place a mark, click on an empty square on the board. If the square is already occupied, nothing will happen. The game will continue until one player wins or the board is full (a tie).

## Code Explanation

The game logic is implemented in the `tictactoe.py` file. Here's a brief explanation of the code:

- The `ROWS` and `COLUMNS` variables define the dimensions of the board.
- The `WIDTH` and `HEIGHT` variables define the dimensions of the game window.
- The `CIRCLE` and `CROSS` variables load the images for the marks.
- The `mark` function updates the board with the player's mark.
- The `is_valid_mark` function checks if a given position on the board is empty.
- The `is_board_full` function checks if the board is full.
- The `draw_board` function draws the board on the screen.
- The `draw_lines` function draws the lines that separate the squares on the board.
- The `is_winning_move` function checks if a player has won the game.

The game loop is implemented using Pygame's event loop. The loop listens for events (such as mouse clicks) and updates the game state accordingly. The loop also redraws the board and marks on the screen after each update.

## Credits

The images for the marks are taken from Wikipedia: https://en.wikipedia.org/wiki/File:X_mark.svg and https://en.wikipedia.org/wiki/File:O_mark.svg


