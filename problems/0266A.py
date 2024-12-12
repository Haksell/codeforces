# ruff: noqa: E731, E741
from itertools import groupby

input()
print(sum(sum(1 for _ in v) - 1 for _, v in groupby(input())))
