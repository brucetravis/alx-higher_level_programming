#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints a message containing the first and last names.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Default is an empty string.

    Returns:
        None

    Raises:
        TypeError: If first_name or last_name is not a string.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter", "White")
        My name is Walter White
        >>> say_my_name("Bob")
        My name is Bob
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    full_name = first_name + " " + last_name if last_name else first_name
    print("My name is", full_name)

if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
