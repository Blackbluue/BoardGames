#!/usr/bin/env python3
"""board module."""


class Board:
    """Docstring for Board."""

    def __init__(self):
        """Initialize object."""
        self._positions = [["", "", ""], ["", "", ""], ["", "", ""]]

    def place(self, token, pos):
        """Place a token at the specifed position.

        pos is a 2-size tuple containing an x,y coordinate.
        """
        if (self._positions[pos[0]][pos[1]] == ""):
            self._positions[pos[0]][pos[1]] = token

    def check_win(self):
        """Check if the game has ended."""
        return False

    def get_board_view(self):
        """Return a read-only view of the board as a tuple of tuples."""
        temp = list()
        for row in self._positions:
            new_row = tuple(row)
            temp.append(new_row)
        return tuple(temp)
