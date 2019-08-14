#!/usr/bin/env python3
"""base module."""
from games.connect4.board import Board
from games.connect4.player import Player


def main():
    """Control program flow."""
    board = Board()
    player1 = Player("x")
    player2 = Player("o")
    turn = 1

    while True:
        print(board)
        if turn % 2 != 0:
            current_player = player1
        else:
            current_player = player2
        pos = play_turn(current_player, board)
        if board.check_win(*pos):
            print(board)
            print("Player %s has won!" % current_player)
            break
        else:
            turn += 1
    return


def play_turn(player, board):
    """Allows a player to make a move. Returns the position played."""
    column = get_col(player.get_token())
    position = board.place(player.get_token(), column)
    while not position:  # position is None if column is full and token not placed
        print("Column %s is full" % column)
        column = get_col(player.get_token())
        position = board.place(player.get_token(), column)
    return position


def get_col(player):
    """Get user input for board position."""
    # need to add input validation
    return int(input("Player %s choose a column: " % player))


if __name__ == "__main__":
    main()
