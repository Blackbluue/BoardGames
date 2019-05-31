#!/usr/bin/env python3
"""base module."""
from board import Board
from player import Player


def main():
    """Control program flow."""
    board = Board()
    player1 = Player("x")
    player2 = Player("o")

    while (not board.check_win()):
        pass
    return


def play_turn(player):
    """."""
    position = input("Choose a position to play: ")

if __name__ == "__main__":
    main()
