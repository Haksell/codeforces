# ruff: noqa: E731, E741
from itertools import combinations, product
from math import gcd, isqrt
from random import randint, sample
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive(n, s):
    for a in product(reversed(s), repeat=n):
        if all(
            a[gcd(i + 1, j + 1) - 1] != gcd(a[i], a[j])
            for i in range(n)
            for j in range(i + 1, n)
        ):
            return list(a)
    return [-1]


N = 10**5 + 1
bd = list(range(N))
for i in range(2, isqrt(N) + 1):
    if bd[i] == i:
        for j in range(i * i, N, i):
            bd[j] = i


def divisors(n):
    res = 0
    while n > 1:
        d = bd[n]
        n //= d
        res += 1
    return res


def genius(n, s):
    res = []
    for i in range(1, n + 1):
        d = divisors(i)
        if d >= len(s):
            return [-1]
        res.append(s[~d])
    return res


def main():
    MODE = 2
    if MODE == 0:
        for n in range(1, 10):
            for m in range(1, n + 1):
                for s in combinations(range(1, n + 1), r=m):
                    rn = naive(n, s)
                    rs = genius(n, s)
                    print(n, s, rn, rs)
                    if rn != rs:
                        return
    elif MODE == 1:
        for _ in range(100):
            n = randint(1, 10)
            m = randint(1, n)
            s = sorted(sample(range(1, n + 1), k=m))
            rn = naive(n, s)
            rs = genius(n, s)
            print(n, s, rn, rs)
            if rn != rs:
                return
    else:
        for _ in rir():
            n, m = mir()
            s = lmir()
            print(*genius(n, s))


if __name__ == "__main__":
    main()
