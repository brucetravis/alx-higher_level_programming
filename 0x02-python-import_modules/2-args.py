#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]

    num_arguments = len(arguments)

    print("{} argument{}{}".format(
        num_arguments,
        "" if num_arguments == 1 else "s",
        ":" if num_arguments > 0 else ""))

    if num_arguments == 0:
        print()
    else:
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))
