#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a count to keep track of the printed integers

    try:
        for i in range(x):
            # Check if the element at the current index is an integer
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1  # Increment the count of printed integers

        print()  # Print a newline after printing all integers

    except IndexError:
        pass  # Handle the case where x is greater than the available elements

    return count
