# ruff: noqa: E731, E741
import math


def smallest_prime_factor(n):
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            return d
    return n


for _ in range(int(input())):
    lo, hi = map(int, input().split())
    if hi <= 3:
        print(-1)
    elif lo == hi:
        spf = smallest_prime_factor(hi)
        if spf == hi:
            print(-1)
        else:
            first = hi // spf
            print(first, hi - first)
    else:
        print(hi >> 1, hi >> 1)
