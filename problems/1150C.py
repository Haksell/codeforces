# ruff: noqa: E731, E741
from itertools import combinations
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def is_prime(n):
    return n >= 2 and all(n % i for i in range(2, isqrt(n) + 1))


def score(a):
    x = 0
    res = 0
    for ai in a:
        x += ai
        res += is_prime(x)
    return res


def naive(c1, c2):
    best = -1
    res = []
    for c in combinations(range(c1 + c2), r=c1):
        a = [2] * (c1 + c2)
        for i in c:
            a[i] = 1
        s = score(a)
        if s > best:
            best = s
            res = a
    return res


def smart(c1, c2):
    if c1 == 0:
        return [2] * c2
    if c2 == 0:
        return [1] * c1
    return [2, 1] + [2] * (c2 - 1) + [1] * (c1 - 1)


def main():
    n = ir()
    a = lmir()
    c1 = a.count(1)
    c2 = n - c1
    print(*smart(c1, c2))


def test():
    for c1 in range(10):
        for c2 in range(10):
            rn = naive(c1, c2)
            rs = smart(c1, c2)
            sn = score(rn)
            ss = score(rs)
            if sn != ss:
                print(f"naive({c1}, {c2}): {rn} ({sn})")
                print(f"smart({c1}, {c2}): {rs} ({ss})")
                return


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
