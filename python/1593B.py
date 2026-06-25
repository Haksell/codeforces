# ruff: noqa: E731, E741
from math import inf


def f(n, a, b):
    first = True
    for i, c in enumerate(reversed(n)):
        if first:
            if c == b:
                first = False
        else:
            if c == a:
                return i - 1
    return inf


for _ in range(int(input())):
    n = input()
    print(min(f(n, "0", "0"), f(n, "2", "5"), f(n, "5", "0"), f(n, "7", "5")))
