from sys import argv

try:
    args = argv[1:]
    a, b = int(args[0]), int(args[1])
    print(a + b)
except Exception:
    print(0)