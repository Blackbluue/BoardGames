#!/usr/bin/env python3
"""Tic Tac Toe game board module."""
import pygame
import games.base.board
from games.gui.globals import BLACK

class Board(games.base.board.Board):
    """Board for Tic-Tac-Toe."""

    def __init__(self):
        """Initialize object."""
        super().__init__(row_c=3, col_c=3, row_p=100, col_p=100)
        self._player = "X"
        self._tokens["X"] = pygame.image.load("games/tictactoe/X.png").convert()
        self._tokens["O"] = pygame.image.load("games/tictactoe/O.gif").convert()
        pygame.display.set_caption("Tic Tac Toe")

    def check_win(self, row, col):
        """Check if the game has ended."""
        view = self.get_board_view()
        # check if previous move caused a win on vertical line
        if view[0][col] == view[1][col] == view [2][col]:
            return True
        # check if previous move caused a win on horizontal line
        if view[row][0] == view[row][1] == view[row][2]:
            return True
        # check if previous move was on the reverse diagonal and caused a win
        if row == col and view[0][0] == view[1][1] == view[2][2]:
            return True
        # check if previous move was on the forward diagonal and caused a win
        if row + col == 2 and view[0][2] == view[1][1] == view[2][0]:
            return True
        return False  # game not finished

    def place_token(self, x, y):
        """Place a token on the board based on the position of the mouse."""
        winner = None
        grid_x, grid_y = self.convert_to_grid(x, y)
        print(f"Player {self._player} clicked grid point ({grid_x}, {grid_y})")

        if self.set(grid_x, grid_y, self._player) is None:
            print("That space is taken")
            winner = None
        elif self.check_win(grid_x, grid_y):
            winner = self._player
        else:
            self._player = "O" if self._player == "X" else "X"

        return winner

    def __str__(self):
        """String representation of the object."""
        CELL_WIDTH = 3  # cell value + both side walls
        COL_COUNT = 3  # Tic Tac Toe has 3 columns
        sep = '-' * CELL_WIDTH * COL_COUNT  # seperator between each row
        str_view = sep + '\n'
        for row in self.get_board_view():
            for cell in row:
                str_view += "|" + cell + "|"
            str_view += '\n' + sep + '\n'
        return str_view.rstrip()
