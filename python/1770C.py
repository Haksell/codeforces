# ruff: noqa: E731, E741
from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import gcd
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive(a):
    return any(
        all(gcd(a[i] + k, a[j] + k) == 1 for i, j in combinations(range(len(a)), r=2))
        for k in range(1, 101)
    )


def all_coprime(a):
    return all(gcd(a[i], a[j]) == 1 for i, j in combinations(range(len(a)), r=2))


def smart(a):
    cnt = Counter(a)
    if any(v > 1 for v in cnt.values()):
        return False
    for m in range(2, 51):
        d = [0] * m
        for x in a:
            d[x % m] += 1
        if all(di >= 2 for di in d):
            return False
    return True


debug = False
if debug:
    for args in combinations_with_replacement(range(1, 12), 5):
        nn = naive(args)
        ss = smart(args)
        if nn != ss:
            print(args, "|", nn, ss)
else:
    for _ in rir():
        n = ir()
        a = lmir()
        print("YES" if smart(a) else "NO")
