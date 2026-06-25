# ruff: noqa: E731, E741
from itertools import product
from math import factorial
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))
MOD = 998244353


def f(s):
    extension = [""] * (2 * len(s) - 1)
    for i, c in enumerate(s):
        extension[i << 1] = c
    ans = 0
    for l in product("01", repeat=len(s) - 1):
        for i, b in enumerate(l):
            extension[2 * i + 1] = b
        o = z = 0
        for i, c in enumerate(extension):
            o += c == "0"
            z += c == "1"
            if i & 1 == 0 and ((c == "0" and o < z) or (c == "1" and z < o)):
                break
        else:
            ans += 1
    return ans


def naive(n, s):
    return sum(f(s[: i + 1]) for i in range(n)) % MOD


def choose(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


def smart(n, s):
    ext = ans = 1
    for a, b in zip(s, s[1:]):
        if a == b:
            ext = 2 * ext % MOD
        else:
            ext = 1
        ans += ext
    return ans % MOD


debug = False
if debug:
    for s in product("01", repeat=5):
        args = [len(s), s]
        nn = naive(*args)
        ss = smart(*args)
        if True or nn != ss:
            print(args, "|", "GOOD" if nn == ss else "BAD ", nn, ss)
else:
    for _ in rir():
        n = ir()
        s = read().strip()
        print(smart(n, s))
