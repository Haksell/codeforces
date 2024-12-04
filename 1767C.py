# ruff: noqa: E731, E741
from functools import cache
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))
MOD = 998_244_353


def naive():
    return


def smart(n, a):
    for r in a:
        if 1 in r and 2 in r:
            i1 = [i for i, x in enumerate(r) if x == 1][-1]
            i2 = r.index(2)
            if i2 < i1:
                return 0

    @cache
    def helper(i, l0, l1):
        if i == n:
            return 1
        b0 = b1 = True
        for j, r in enumerate(a[: i + 1]):
            cond = r[i]
            if cond == 1:
                if l0 >= j:
                    b1 = False
                if l1 >= j:
                    b0 = False
            elif cond == 2:
                if l0 < j:
                    b1 = False
                if l1 < j:
                    b0 = False
        ans = 0
        if b0:
            ans += helper(i + 1, i, l1)
        if b1:
            ans += helper(i + 1, l0, i)
        return ans % MOD

    a = [[0] * i + r for i, r in enumerate(a)]
    return helper(0, -1, -1)


debug = False
if debug:
    for _ in []:
        args = []
        nn = naive(*args)
        ss = smart(*args)
        if nn != ss:
            print(args, "|", nn, ss)
else:
    n = ir()
    a = [lmir() for _ in range(n)]
    print(smart(n, a))
