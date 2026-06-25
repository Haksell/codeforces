# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def get_primes(n):
    s = [True] * n
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            for j in range(i * i, n, i):
                s[j] = False
    return [i for i, b in enumerate(s) if i >= 2 and b]


def main():
    primes = get_primes(10**5 + 1)
    for _ in rir():
        m = n = ir()
        f = dict()
        for p in primes:
            c = 0
            while n % p == 0:
                c += 1
                n //= p
            if c:
                f[p] = c
        if n > 1:
            f[n] = 1
        k = max(f, key=f.get)
        res = []
        for _ in range(f[k] - 1):
            res.append(k)
            m //= k
        res.append(m)
        print(len(res))
        print(*res)


if __name__ == "__main__":
    main()
