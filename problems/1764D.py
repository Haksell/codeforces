# ruff: noqa: E731, E741
from functools import cache
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

n, p = mir()
FACT = [1]
for i in range(1, 10000):
    FACT.append(i * FACT[-1] % p)


@cache
def pc(b, e, p):
    return pow(b, e, p)


def naive(n, p):
    ans = 0 if n & 1 else FACT[n - 2]
    for last in range(1, n + 1 >> 1):
        x = last if n & 1 else last + 1
        c = 1
        for i in range(last):
            ans += x * c * FACT[n - i - 3]
            c = c * (last - 1 - i) % p * pc(i + 1, -1, p) % p
        ans %= p
    return ans * n % p


print(naive(n, p))
