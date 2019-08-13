#!/usr/bin/env python3
"""Connect 4 game board module."""
import games.base.board


class Board(games.base.board.Board):
    """Board for Connect 4."""

    ROW_COUNT = 6
    COL_COUNT = 7
    EMPTY_CELL = " "

    def __init__(self):
        """Initialize object."""
        super().__init__(row_count=self.ROW_COUNT, col_count=self.COL_COUNT,
                         empty_cell=self.EMPTY_CELL)

    def check_win(self, x, y):
        """Check if the game has ended."""
        return False  # unfinished


    def place(self, token, col):
        """Place a token at the first open spot of the specified column.

        Return the position of the cell where the token was placed, or None if
        the column was full and token was not placed."""
        for row in range(self.ROW_COUNT - 1, -1, -1):  # iterate through the rows backwards
            if self.get(row, col) == self.EMPTY_CELL:  # find the first empty cell
                super().place(token, row, col)  # place token in that cell
                return (row, col)
        return None


    def __str__(self):
        """String representation of the object."""
        CELL_WIDTH = 3  # cell value + both side walls
        COL_COUNT = 7  # Tic Tac Toe has 3 columns
        sep = '-' * CELL_WIDTH * COL_COUNT  # seperator between each row
        str_view = sep + '\n'
        for row in self.get_board_view():
            for cell in row:
                str_view += "|" + cell + "|"
            str_view += '\n' + sep + '\n'
        return str_view.rstrip()
