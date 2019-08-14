#!/usr/bin/env python3
"""base module."""
from games.checkers.board import Board
from games.checkers.player import Player


def main():
    """Control program flow."""
    player1 = Player("x")
    player2 = Player("o")
    board = Board(player1, player2)
    turn = 1

    while True:
        print(board)
        if turn % 2 != 0:
            attacker = player1
            defender = player2
        else:
            attacker = player2
            defender = player1
        play_turn(attacker, board)
        if defender.token_total() == 0:
            print(board)
            print("Player %s has won!" % attacker)
            break
        else:
            turn += 1
    return


def play_turn(player, board):
    """Allows a player to make a move."""
    get_move(player, board)  # unfinished


def get_move(player, board):
    """Get input form player on where to move."""
    # need to add input validation
    position = input("Player %s choose the position of a piece to move: " % player).split(',')
    piece = board.get((int(char) for char in position))
    position = input("Player %s choose the position to move the piece: " % player).split(',')
    move_to_row, move_to_col = (int(char) for char in position)


if __name__ == "__main__":
    main()
