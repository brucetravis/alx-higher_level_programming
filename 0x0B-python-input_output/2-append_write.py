#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file
    (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the text file to 
        which the text will be appended.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added


if __name__ == "__main__":
    nb_characters_added = append_write(
            "file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
