# ruff: noqa: E731, E741
from math import floor, log10

for _ in range(int(input())):
    n = int(input())
    print(n - 10 ** floor(log10(n)))
