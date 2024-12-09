# ruff: noqa: E731, E741
from itertools import cycle, islice

for _ in range(int(input())):
    n = int(input())
    print("9" + "".join(islice(cycle("8901234567"), n - 1)))
