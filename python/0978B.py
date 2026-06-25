# ruff: noqa: E731, E741
from itertools import groupby

input()
s = input()
print(sum(max(0, len(list(v)) - 2) for k, v in groupby(s, lambda c: c == "x") if k))
