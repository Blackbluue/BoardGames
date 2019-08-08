#!/usr/bin/env python3
"""board module."""


class Board:
    """Base board class."""

    def __init__(self, row_count, col_count, empty_cell=" "):
        """Initialize object."""
        self._EMPTY_CELL = empty_cell
        self._positions = [[empty_cell for col in range(col_count)] for row in range(row_count)]

    def place(self, token, pos):
        """Place a token at the specifed position.

        pos is a 2-size iterable containing an x,y coordinate.
        """
        self._positions[pos[0]][pos[1]] = token

    def check_win(self):
        """Check if the game has ended."""
        return False  # method not finished

    def get_board_view(self):
        """Return a read-only view of the board as a tuple of tuples."""
        return tuple(tuple(cell for cell in row) for row in self._positions)
