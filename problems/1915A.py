# ruff: noqa: E731, E741
from functools import reduce
from operator import xor

for _ in range(int(input())):
    print(reduce(xor, map(int, input().split())))
