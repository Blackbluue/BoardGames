#!/usr/bin/env python3
"""base module."""
from games.tictactoe.board import Board
from games.tictactoe.player import Player


def main():
    """Control program flow."""
    board = Board()
    player1 = Player("x")
    player2 = Player("o")
    turn = 1

    while (not board.check_win()):
        print(board)
        if turn % 2 != 0:
            current_player = player1
        else:
            current_player = player2
        pos = play_turn(current_player, board)
        turn += 1
    return


def play_turn(player, board):
    """Allows a player to make a move. Returns the position played."""
    position = get_pos(player.get_token())
    board.place(player.get_token(), position)
    return position


def get_pos(player):
    """Get user input for board position."""
    # need to add input validation
    position = input("Player %s choose a position to play: " % player).split(',')
    return tuple(int(char) for char in position)

if __name__ == "__main__":
    main()
