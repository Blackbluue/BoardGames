#!/usr/bin/env python3
"""Tic Tac Toe game board module."""
import games.base.board


class Board(games.base.board.Board):
    """Board for Tic-Tac-Toe."""

    def __init__(self):
        """Initialize object."""
        super().__init__(row_count=3, col_count=3)

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
