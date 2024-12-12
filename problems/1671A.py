# ruff: noqa: E731, E741
from itertools import groupby

for _ in range(int(input())):
    print("YES" if all(sum(1 for _ in v) != 1 for _, v in groupby(input())) else "NO")
