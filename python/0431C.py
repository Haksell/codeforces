# ruff: noqa: E731, E741
from functools import cache


@cache
def f(n, b):
    return (
        int(n == 0 and b)
        if n <= 0
        else sum(f(n - i, b or i >= d) for i in range(1, k + 1)) % MOD
    )


MOD = 1_000_000_007
n, k, d = map(int, input().split())
print(f(n, False))
