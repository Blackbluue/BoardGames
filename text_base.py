#!/usr/bin/env python3
"""base module."""
from games.tictactoe.board import Board
from games.tictactoe.player import Player


def main():
    """Control program flow."""
    board = Board()
    player1 = Player("x")
    player2 = Player("o")

    while (not board.check_win()):
        print(board)
        play_turn(player1, board)
    return


def play_turn(player, board):
    """."""
    position = get_pos()
    print(position)
    board.place(player.get_token(), position)


def get_pos():
    """Get user input for board position."""
    # need to add input validation
    position = input("Choose a position to play: ").split(',')
    return tuple(int(char) for char in position)

if __name__ == "__main__":
    main()
