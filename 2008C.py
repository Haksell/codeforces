# ruff: noqa: E741, E731

from itertools import count
import math
from random import randint
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


# def f(n):
#     tot = 0
#     for i in count():
#         tot += i
#         if tot > n:
#             return i


def g(n):
    return round(math.sqrt(2 * n + 1))


# for i in [*range(1000), *[randint(1, 10**9) for _ in range(1000)]]:
#     assert f(i) == g(i), (i, f(i), g(i))


for _ in rir():
    l, r = mir()
    print(g(r - l))
