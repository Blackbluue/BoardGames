#!/usr/bin/env python3
"""Tic Tac Toe game board module."""
import games.base.board


class Board(games.base.board.Board):
    """Board for Tic-Tac-Toe."""

    def __init__(self):
        """Initialize object."""
        super().__init__(row_count=3, col_count=3)

    def check_win(self, x, y):
        """Check if the game has ended."""
        view = self.get_board_view()
        # check if previous move caused a win on vertical line
        if view[0][y] == view[1][y] == view [2][y]:
            return True
        # check if previous move caused a win on horizontal line
        if view[x][0] == view[x][1] == view[x][2]:
            return True
        # check if previous move was on the reverse diagonal and caused a win
        if x == y and view[0][0] == view[1][1] == view[2][2]:
            return True
        # check if previous move was on the forward diagonal and caused a win
        if x + y == 2 and view[0][2] == view[1][1] == view[2][0]:
            return True
        return False  # game not finished

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
