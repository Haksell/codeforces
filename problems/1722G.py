# ruff: noqa: E731, E741
from functools import reduce
from operator import xor

for _ in range(int(input())):
    l = list(range(int(input())))
    l[-1] ^= reduce(xor, l)
    l[-1] |= 1 << 20
    l[-3] |= 1 << 20
    print(*l)
