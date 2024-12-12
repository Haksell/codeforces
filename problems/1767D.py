# ruff: noqa: E731, E741
from itertools import permutations, product
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def simulate(perm, s):
    for c in s:
        f = [min, max][int(c)]
        perm = [f(x, y) for x, y in zip(perm[0::2], perm[1::2])]
    return perm[0]


def naive(n, s):
    winners = set()
    for perm in permutations(range(1 << n)):
        winners.add(simulate(perm, s))
    return [w + 1 for w in sorted(winners)]  # +1


def smart(n, s):
    perm = list(range(1 << n))
    z = s.count("0")
    o = s.count("1")
    rm0 = 2**z - 1
    rm1 = 2**o - 1
    perm = perm[rm1:]
    perm = perm[: len(perm) - rm0]
    return [w + 1 for w in perm]  # +1


debug = False
if debug:
    n = 3
    for s in product("01", repeat=n):
        args = [n, s]
        nn = naive(*args)
        ss = smart(*args)
        if nn != ss:
            print(args, "|", nn, ss)
else:
    n = ir()
    s = read().strip()
    print(*smart(n, s))
