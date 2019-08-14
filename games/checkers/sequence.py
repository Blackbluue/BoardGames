#!/usr/bin/env python3
"""sequence module."""


class Sequence:
    """Defines the sequence of moves for a player in Checkers."""

    def __init__(self, board, piece, enemy_list, promoted=False):
        """Initialize the object."""
        self._board = board
        self._piece = piece
        self._enemy_list = enemy_list
        self._promoted = promoted
        self._queue = []

    def add_move(self, row, col):
        """Add a move for this sequence."""
        move = _Move(self._board, self._piece, self._enemy_list, self._promoted, row, col)
        self._queue.append(move)

    def execute(self):
        """Execute all queued moves."""
        for move in self._queue:
            move.execute()

class _Move:
    """Defines a single move."""

    def __init__(self, board, piece, enemy_list, row, col, promoted=False):
        """Initialize the object."""
        self._board = board
        self._piece = piece
        self._enemy_list = enemy_list
        self._promoted = promoted
        self._row = row
        self._col = col

    def execute(self):
        """Execute this move."""
