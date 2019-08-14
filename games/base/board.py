#!/usr/bin/env python3
"""board module."""


class Board:
    """Base board class."""

    def __init__(self, row_count, col_count, empty_cell=" "):
        """Initialize object."""
        self._EMPTY_CELL = empty_cell
        self._positions = [[empty_cell for col in range(col_count)] for row in range(row_count)]

    def place(self, token, row, col):
        """Place a token at the specifed position.

        Return the position the token was placed in if operation successful."""
        self._positions[row][col] = token
        return (row, col)

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
