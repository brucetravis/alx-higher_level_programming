#!/usr/bin/python3

"""
This module defines a class MyList that inherits from list and provides a method to print the list in sorted order.
"""

class MyList(list):
    def print_sorted(self):
        """
        This method prints the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == "__main__":
    MyList = __import__('1-my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    print(my_list)  # Output: [1, 4, 2, 3, 5]
    my_list.print_sorted()  # Output: [1, 2, 3, 4, 5]
    print(my_list)  # Output: [1, 4, 2, 3, 5]
