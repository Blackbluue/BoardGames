#!/usr/bin/env python3
"""player module."""


class Player:
    """Player for Connect 4."""

    def __init__(self, token):
        """Initialize object."""
        self._token = token.upper()

    def get_token(self):
        """Return the token of this player."""
        return self._token

    def __repr__(self):
        """String representation of the object."""
        return self.get_token()
