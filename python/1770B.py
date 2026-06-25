# ruff: noqa: E731, E741
from collections import deque
from itertools import permutations
from math import inf
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def get_cost(p, n, k):
    c = [max(p[i : i + k]) + min(p[i : i + k]) for i in range(n - k + 1)]
    return max(c)


def naive(n, k):
    best = inf
    res = []
    for p in permutations(range(1, n + 1)):
        cost = get_cost(p, n, k)
        if cost < best:
            best = cost
            res = [p]
            # print(n, k, cost, p, c)
        elif cost == best:
            res.append(p)
    # print(n, k, best, len(res), res)
    # print()
    return res[0]


def smart(n, k):
    res = []
    d = deque(range(1, n + 1))
    for i in range(n):
        res.append(d.popleft() if i % k == 1 else d.pop())
    return res


debug = False
if debug:
    for n in range(1, 9):
        for k in range(1, n + 1):
            args = [n, k]
            nn = naive(*args)
            ss = smart(*args)
            if get_cost(nn, n, k) != get_cost(ss, n, k):
                print(args, "|", max(nn), nn, max(ss), ss)
else:
    for _ in rir():
        n, k = mir()
        print(*smart(n, k))
