# ruff: noqa: E731, E741
from itertools import chain

n = int(input())
for i in chain(range(n + 1), reversed(range(n))):
    print("  " * (n - i), end="")
    print(*range(i + 1), *reversed(range(i)))
