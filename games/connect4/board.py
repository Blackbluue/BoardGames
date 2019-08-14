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

    def check_win(self, row, col):
        """Check if the game has ended."""
        view = self.get_board_view()
        # check if previous move caused a win on vertical line
        start = 0  # start of check
        for row_chk in range(start, self.ROW_COUNT - 3):  # loop through possible start points
            if view[row_chk][col] == view[row_chk + 1][col] == view [row_chk + 2][col] == view [row_chk + 3][col]:
                if view[row_chk][col] != self.EMPTY_CELL:
                    return True
        # check if previous move caused a win on horizontal line
        start = 0  # start of check
        for col_chk in range(start, self.COL_COUNT - 3):  # loop through possible start points
            if view[row][col_chk] == view[row][col_chk + 1] == view [row][col_chk + 2] == view [row][col_chk + 3]:
                if view[row][col_chk] != self.EMPTY_CELL:
                    return True
        # check if previous move was on a reverse diagonal and caused a win
        if self._check_rev_diag(view, row, col):
            return True
        # check if previous move was on a forward diagonal and caused a win
        if self._check_fwd_diag(view, row, col):
            return True
        return False  # game not won

    def _check_rev_diag(self, view, row, col):
        """Check reverse diagnals for win conditions."""
        # reverse diagnals cannot cause a win in these positions, dont check
        invalid_win = [(0, 4), (0, 5), (0, 6), (1, 5), (1, 6), (2, 6),
                       (5, 0), (5, 1), (5, 2), (4, 0), (4, 1), (3, 0)]
        if (row, col) in invalid_win:
            return False
        # get coord for start of diagnal (row, col)
        row_chk, col_chk = row, col
        while row_chk > 0 and col_chk > 0:
            row_chk -= 1
            col_chk -= 1
        # increment start until start is 4 cells from diagnal edge of board
        while row_chk <= self.ROW_COUNT - 4 and col_chk <=  self.COL_COUNT - 4:
            if view[row_chk][col_chk] == view[row_chk + 1][col_chk + 1] == view [row_chk + 2][col_chk + 2] == view [row_chk + 3][col_chk + 3]:
                if view[row_chk][col_chk] != self.EMPTY_CELL:
                    return True
            row_chk += 1
            col_chk += 1
        return False  # win conditions not met

    def _check_fwd_diag(self, view, row, col):
        """Check forward diagnals for win conditions."""
        # forward diagnals cannot cause a win in these positions, dont check
        invalid_win = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0),
                       (5, 4), (5, 5), (5, 6), (4, 5), (4, 6), (3, 6)]
        if (row, col) in invalid_win:
            return False
        # get coord for start of diagnal (row, col)
        row_chk, col_chk = row, col
        while row_chk > 0 and col_chk < self.COL_COUNT - 1:
            row_chk -= 1
            col_chk += 1
        # increment start until start is 4 cells from diagnal edge of board
        while row_chk <= self.ROW_COUNT - 4 and col_chk >=  3:
            if view[row_chk][col_chk] == view[row_chk + 1][col_chk - 1] == view [row_chk + 2][col_chk - 2] == view [row_chk + 3][col_chk - 3]:
                if view[row_chk][col_chk] != self.EMPTY_CELL:
                    return True
            row_chk += 1
            col_chk -= 1
        return False  # win conditions not met

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
        sep = '-' * CELL_WIDTH * self.COL_COUNT  # seperator between each row
        str_view = sep + '\n'
        for row in self.get_board_view():
            for cell in row:
                str_view += "|" + cell + "|"
            str_view += '\n' + sep + '\n'
        return str_view.rstrip()
