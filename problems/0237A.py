# ruff: noqa: E731, E741
from itertools import groupby
import sys

a = sys.stdin.read().split("\n")[1:-1]
print(max(sum(1 for _ in v) for _, v in groupby(a)))
