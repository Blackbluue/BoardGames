#!/usr/bin/env python3
"""testing module."""
import pygame
from games.tictactoe.board import Board

# Build board and display window
b = Board()
winner = None

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            winner = b.place_token(x, y)

    # --- Game logic should go here
    if winner is not None:
        print(f"Player {winner} has won the game!")
        done = True
    # --- Drawing code should go here
    b.draw_board()

    # --- Limit to 60 frames per second
    clock.tick(60)
