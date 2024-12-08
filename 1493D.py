# ruff: noqa: E731, E741
from collections import defaultdict
from functools import reduce
from math import gcd
import sys

mir = lambda: map(int, sys.stdin.readline().split())

MOD = 10**9 + 7
SIZE = 200001
SIEVE = [True] * SIZE
SIEVE[0] = SIEVE[1] = False
for i in range(2, SIZE):
    if SIEVE[i]:
        for j in range(i * i, SIZE, i):
            SIEVE[j] = False
PRIMES = [n for n, b in enumerate(SIEVE) if b]


def prime_factors(n):
    d = defaultdict(int)
    for p in PRIMES:
        if p * p > n:
            break
        while n % p == 0:
            n //= p
            d[p] += 1
    if n > 1:
        d[n] += 1
    return dict(d)


n, q = mir()
a = list(mir())
g = reduce(gcd, a)
factors = prime_factors(g)
counts = {p: defaultdict(int) for p in PRIMES}
alive = {p: 0 for p in PRIMES}
l = []
for x in a:
    d = prime_factors(x)
    for k, v in d.items():
        counts[k][v] += 1
        alive[k] += 1
    l.append(d)
output = []
for _ in range(q):
    i, x = mir()
    i -= 1
    for k, v in prime_factors(x).items():
        old = l[i].get(k, 0)
        l[i][k] = new = old + v
        if old == 0:
            alive[k] += 1
        counts[k][new] += 1
        counts[k][old] = max(0, counts[k][old] - 1)
        if counts[k][old] == 0:
            del counts[k][old]
            mini = 0 if alive[k] < n else min(counts[k])
            if mini > factors.get(k, 0):
                g *= k ** (mini - old)
                factors[k] = mini
    g %= MOD
    output.append(g)
sys.stdout.write("\n".join(map(str, output)))
