# ruff: noqa: E731, E741
from functools import cache
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

N = 1_000_001
sieve = [True] * N
sieve[0] = sieve[1] = False
for i in range(2, isqrt(N) + 1):
    if sieve[i]:
        for j in range(i * i, N, i):
            sieve[j] = False
primes = [i for i, b in enumerate(sieve) if b]


def naive(n, d, s):
    @cache
    def h(s):
        res = s
        for t in range(2 * s, n + 1, s):
            if t > n or (t - s) > d:
                break
            res = max(res, h(t))
        return res

    return h(s)


@cache
def nos(n, d):
    if d == 0:
        return 1
    if 2 * d <= n:
        return 2 * d
    if d >= n - 1:
        return n
    if n & 1 == 0:
        return n
    for p in primes:
        if n % p == 0 and (p - 1) * n <= p * d:
            return n
    return n - 1


def smart(n, d, s):
    return s * nos(n // s, d // s)


def main():
    n, d, s = mir()
    print(smart(n, d, s))


def test():
    for n in range(2, 200):
        for d in range(1, n):
            for s in range(1, n + 1):
                a = naive(n, d, s)
                b = smart(n, d, s)
                if a != b:
                    print(n, d, s, "|", a, b)
                    return


if __name__ == "__main__":
    main()
