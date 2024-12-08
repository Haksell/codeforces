# ruff: noqa: E731, E741
from itertools import combinations
from math import isqrt


LIM = 1_000_000
sieve = [True] * LIM
sieve[0] = sieve[1] = False
for i in range(2, isqrt(LIM) + 1):
    if sieve[i]:
        for j in range(i * i, LIM, i):
            sieve[j] = False


def is_prime(n):
    return sieve[n] if n < LIM else all(n % i for i in range(2, isqrt(n) + 1))


def solve(n):
    n = list(map(str, n))
    for digits in range(1, len(n) + 1):
        for comb in combinations(range(len(n)), r=digits):
            m = int("".join(n[c] for c in comb))
            if not is_prime(m):
                return m
    return f"{n} NO"


for _ in range(int(input())):
    k = int(input())
    n = input()
    ans = solve(n)
    print(len(str(ans)))
    print(ans)
