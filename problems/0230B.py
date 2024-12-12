# ruff: noqa: E731, E741
import sys
from math import isqrt


def t_prime(n):
    return isqrt(n) ** 2 == n and sieve[isqrt(n)]


size = 10**6 + 1
sieve = [True] * size
sieve[0] = sieve[1] = False
for i in range(size):
    if sieve[i]:
        for j in range(i * i, size, i):
            sieve[j] = False

input()
a = list(map(int, sys.stdin.read().split()))
sys.stdout.write("\n".join("YES" if t_prime(n) else "NO" for n in a))
