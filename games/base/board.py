#!/usr/bin/env python3
"""board module."""
import pygame
from games.gui.globals import WHITE, BLACK, RED, GREEN

pygame.init()

class Board:
    """Base board class."""

    def __init__(self, row_c, col_c, row_p, col_p, empty_cell=" "):
        """Initialize object.

        row_c is number of rows on the grid
        col_c is number of columns on the grid
        these values are arbitrary to window size, and do not relate to pixels.

        row_p is row height in pixels
        col_p is column width in pixels

        empty_cell is what value to place in an initialized empty cell
        defaults to an empty space"""
        self._EMPTY_CELL = empty_cell
        self._positions = [[empty_cell for col in range(col_c)] for row in range(row_c)]

        self._MARGIN = 3
        self._WINDOW_WIDTH = (row_c * row_p) + ((row_c + 1) * self._MARGIN)
        self._WINDOW_HEIGHT = (col_c * col_p) + ((col_c + 1) * self._MARGIN)
        self._ROWS = row_c
        self._COLS = col_c
        self._CELL_W = row_p
        self._CELL_H = col_p

        self._tokens = dict()

        self._screen = pygame.display.set_mode((self._WINDOW_WIDTH, self._WINDOW_HEIGHT))

    def set(self, row, col, token, replace=False):
        """Set the value of the specified cell."""
        if not replace and self._positions[row][col] is not self._EMPTY_CELL:
            return None
        cell = self._positions[row][col]
        self._positions[row][col] = token
        return cell

    def get(self, row, col):
        """Get the value of the specified cell.

        Row and Column indicies start at 0. Negative indecies are valid. If out
        of range of the board, will return None."""
        try:
            cell = self._positions[row][col]
            if cell == self._EMPTY_CELL:
                cell = None
        except IndexError:
            cell = None
        finally:
            return cell

    def get_board_view(self):
        """Return a read-only view of the board as a tuple of tuples."""
        return tuple(tuple(cell for cell in row) for row in self._positions)

    def convert_to_grid(self, x, y):
        """convert mouse coordinates to grid coordinates"""
        grid_x = x // self._CELL_W
        grid_y = y // self._CELL_H
        return (grid_x, grid_y)

    def draw_board(self):
        """Draw the game board."""
        # First, clear the screen to black. Don't put other drawing commands
        # above this, or they will be erased with this command.
        self._screen.fill(BLACK)
        # Draw on the screen several lines 3 pixels wide using a while loop
        x_offset = y_offset = self._MARGIN
        row = 0

        for x in range(x_offset, self._WINDOW_WIDTH, self._CELL_H + self._MARGIN):
            col = 0
            for y in range(y_offset, self._WINDOW_HEIGHT, self._CELL_W + self._MARGIN):
                token = self._positions[row][col]
                if token == self._EMPTY_CELL:
                    pygame.draw.rect(self._screen, WHITE, [x, y, self._CELL_W, self._CELL_H], 0)
                else:
                    self._screen.blit(self._tokens[token], [x, y])
                col += 1
            row += 1
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
