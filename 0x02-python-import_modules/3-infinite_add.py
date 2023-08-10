import sys

arguments = sys.argv[1:]

result = sum(int(arg) for arg in arguments)

print(result)
