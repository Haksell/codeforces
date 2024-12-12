# ruff: noqa: E731, E741
from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    groups = [k for k, v in groupby(input())]
    print("YES" if len(groups) == len(set(groups)) else "NO")
