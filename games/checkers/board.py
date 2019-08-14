#!/usr/bin/env python3
"""Ceckers game board module."""
import games.base.board


class Board(games.base.board.Board):
    """Board for Checkers."""

    ROW_COUNT = 8
    COL_COUNT = 8
    EMPTY_CELL = " "

    def __init__(self, player1, player2):
        """Initialize object."""
        super().__init__(row_count=self.ROW_COUNT, col_count=self.COL_COUNT,
                         empty_cell=self.EMPTY_CELL)
        self._setup_board(player1.get_token(), player2.get_token())

    def _setup_board(self, p1_token, p2_token):
        """Initial setup for pieces on the board."""
        p1_side = lambda row: row < 3
        p2_side = lambda row: row > 4
        black_square = lambda row, col: (row % 2 == 0 and col % 2 != 0) or (row % 2 != 0 and col % 2 == 0)
        for row in range(self.ROW_COUNT):
            for col in range(self.COL_COUNT):
                if p1_side(row) and black_square(row, col):
                    self.place(p1_token, row, col)
                elif p2_side(row) and black_square(row, col):
                    self.place(p2_token, row, col)
                else:
                    continue  # leave cell blank

    def move_piece(self, row, col, direction):
        """Move the piec at the given position in the desired direction.

        If an opposing piece is in the desired direction and can be jumped, the
        selected piece will land directly behind it and this method will return
        the position of the jumped pieced. Otherwise the selected piece will
        one space in the desired direction and this method will return None.
        """

    def __str__(self):
        """String representation of the object."""
        CELL_WIDTH = 3  # cell value + both side walls
        sep = '-' * CELL_WIDTH * self.COL_COUNT  # seperator between each row
        str_view = sep + '\n'
        for row in self.get_board_view():
            for cell in row:
                str_view += "|" + cell + "|"
            str_view += '\n' + sep + '\n'
        return str_view.rstrip()
