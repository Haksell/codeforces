# ruff: noqa: E731, E741
from itertools import groupby

for _ in range(int(input())):
    s = input()
    a = [sum(1 for _ in v) for k, v in groupby(s) if k == "1"]
    print(sum(sorted(a, reverse=True)[::2]))
