#!/usr/bin/env python3
"""base token module."""
import pygame
from games.gui.globals import WHITE, PIX

class Token(pygame.sprite.Sprite):
    def __init__(self, col, row, image=None):
    """ Constructor."""
    super().__init__()

    self._col = col
    self._row = row

    # if an image is given, use it for the sprite.
    # otherwise, use a transparent background
    if image:
        self.image = pygame.image.load(image).convert()
    else:
        self.image = pygame.Surface([PIX, PIX])
        self.image.fill(WHITE)

    self.image.set_colorkey(WHITE)
    self.rect = self.image.get_rect()
