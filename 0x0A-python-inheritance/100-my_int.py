#!/usr/bin/python3


class MyInt(int):
    """
    A class representing a rebellious integer with inverted equality operators.
    """
    def __eq__(self, other):
        """
        Override the equality operator (==) to invert its behavior.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=) to invert its behavior.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
