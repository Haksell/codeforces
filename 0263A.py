# ruff: noqa: E731, E741
from sys import stdin

y, x = next((y, line.index("1") >> 1) for y, line in enumerate(stdin) if "1" in line)
print(abs(2 - y) + abs(2 - x))
