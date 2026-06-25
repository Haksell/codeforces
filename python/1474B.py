# ruff: noqa: E731, E741
from bisect import bisect_right
from math import isqrt


def get_primes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    return [n for n, is_prime in enumerate(sieve) if is_prime]


primes = get_primes(21000)
for _ in range(int(input())):
    d = int(input())
    p1 = primes[bisect_right(primes, d)]
    p2 = primes[bisect_right(primes, p1 + d - 1)]
    print(p1 * p2)
