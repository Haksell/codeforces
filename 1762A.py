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


def f(n):
    if n & 1:
        ans = 0
        while n & 1:
            n >>= 1
            ans += 1
        return ans
    else:
        ans = 0
        while n & 1 == 0:
            n >>= 1
            ans += 1
        return ans


def smart(n, a):
    x = sum(a) & 1
    if x == 0:
        return 0
    return min(map(f, a))


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
        print(smart(n, a))
