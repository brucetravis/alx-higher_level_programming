def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size (length of one side) of the square.

    Returns:
        None

    Raises:
        TypeError: If 'size' is not an integer or is a float.
        ValueError: If 'size' is less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
