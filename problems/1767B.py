# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive():
    return


def smart(n, a):
    l = sorted(a[1:])
    for x in l:
        if x > a[0]:
            a[0] += (x + 1 - a[0]) >> 1
    return a[0]


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
        print(smart(ir(), lmir()))
