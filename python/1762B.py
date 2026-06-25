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
    return


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
        n = ir()
        a = lmir()
        print(n)
        for i, x in enumerate(a, 1):
            target = 1 << x.bit_length()
            print(i, target - x)
