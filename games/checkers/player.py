#!/usr/bin/env python3
"""player module."""


class Player:
    """Player for Checkers."""

    def __init__(self, token):
        """Initialize object."""
        self._token = token.lower()
        self._unpromoted = 12
        self._promoted = 0
        self._total = self._unpromoted + self._promoted

    def get_token(self):
        """Return the token of this player. The token is for an unpromoted piece."""
        return self._token

    def get_promoted_token(self):
        """Return the token of this player. The token is for a promoted piece."""
        return self._token.upper()

    def promote(self):
        """Promote a number of pieces."""
        self._unpromoted -= 1
        self._promoted += 1

    def sacrifice(self, unpromoted_count=0, promoted_count=0):
        """Decrease token count by specified number."""
        self._unpromoted -= unpromoted_count
        self._promoted -= promoted_count
        self._total = self._unpromoted + self._promoted

    def token_total(self):
        """Return the total number of pieces this player has left."""
        return self._total

    def __repr__(self):
        """String representation of the object."""
        return self.get_token()
