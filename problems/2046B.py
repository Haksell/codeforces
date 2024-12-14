# ruff: noqa: E731, E741
from collections import Counter
import math
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(a):
    fuzz = randint(1, 1 << 30)
    c = Counter(ai + fuzz for ai in a)
    c = sorted([[k - fuzz, v] for k, v in c.items()], reverse=True)
    r1 = []
    r2 = []
    r3 = []
    for ai in a:
        if ai == c[-1][0]:
            r1.append(ai)
            r2.extend(r3)
            r3.clear()
            if c[-1][1] == 1:
                c.pop()
            else:
                c[-1][1] -= 1
        else:
            r3.append(ai)
    keep = min(r2, default=-math.inf) + 1
    for r in r3:
        (r1 if r == keep else r2).append(r)
    return r1 + sorted(r + 1 for r in r2)


def main():
    for _ in rir():
        read()
        print(*solve(lmir()))


if __name__ == "__main__":
    main()
