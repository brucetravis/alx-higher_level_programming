#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object for which to retrieve attributes and methods.

    Returns:
        list: A list of strings representing the attributes and methods.
    """
    return dir(obj)


# Test cases
if __name__ == "__main__":
    print("Attributes and methods of int:")
    print(lookup(int))

    print("\nAttributes and methods of float:")
    print(lookup(float))

    print("\nAttributes and methods of object:")
    print(lookup(object))

    print("\nAttributes and methods of list:")
    print(lookup(list))

    class MyClass:
        def dir(self):
            return ["my_class", "is", "empty"]

    print("\nAttributes and methods of MyClass with custom dir method:")
    my_instance = MyClass()
    print(lookup(my_instance))

    class MyClassWithAttributes:
        one_attribute = 89

    print("\nAttributes and methods of MyClassWithAttributes:")
    print(lookup(MyClassWithAttributes))

    class MyClassWithMethod:
        def one_meth(self):
            pass

    print("\nAttributes and methods of MyClassWithMethod:")
    my_instance_with_method = MyClassWithMethod()
    print(lookup(my_instance_with_method))
