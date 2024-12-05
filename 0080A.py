# ruff: noqa: E731, E741
from itertools import count
from math import isqrt


def is_prime(n):
    return all(n % i for i in range(2, isqrt(n) + 1))


n, m = map(int, input().split())
for i in count(n + 1):
    if is_prime(i):
        print("YES" if i == m else "NO")
        break
