# ruff: noqa: E731, E741
from itertools import count, combinations
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def check(a):
    diff = max(a) - min(a)
    return diff * diff == sum(a)


def naive(n):
    for i in count(n):
        for perm in combinations(range(1, i + 1), n):
            if check(perm):
                return list(perm)
    return []


def smart(n):
    if n & 1:
        return [*range(n // 2 + 2, n + 1), *range(n + 3, n + n // 2 + 4)]
    else:
        return [*range(n // 2, n), *range(n + 1, n + n // 2 + 1)]


for _ in rir():
    n = ir()
    print(*smart(n))

"""
2 (1, 3)
3 (3, 6, 7)
4 (2, 3, 5, 6)
5 (4, 5, 8, 9, 10)
6 (3, 4, 5, 7, 8, 9)
7 (5, 6, 7, 10, 11, 12, 13)
8 (4, 5, 6, 7, 9, 10, 11, 12)
9 (6, 7, 8, 9, 12, 13, 14, 15, 16)
10 (5, 6, 7, 8, 9, 11, 12, 13, 14, 15)
11 (7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19)
12 (6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18)
13 (8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22)
14 (7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21)
15 (9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24, 25)
16 (8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24)
"""
