# ruff: noqa: E731, E741
from heapq import heapify, heappop, heappush
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive():
    return


def smart(n, m, a, b):
    a = a.copy()
    heapify(a)
    for x in b:
        heappop(a)
        heappush(a, x)
    return sum(a)


debug = False
if debug:
    for _ in []:
        args = []
        nn = naive(*args)
        ss = smart(*args)
        if nn != ss:
            print(args, "|", nn, ss)
else:
    for _ in rir():
        n, m = mir()
        a = lmir()
        b = lmir()
        print(smart(n, m, a, b))
