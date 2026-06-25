# ruff: noqa: E731, E741
import math
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MOD = 1_000_000_007

for _ in rir():
    n = ir()
    a = lmir()
    s = sum(a)
    p = sum(ai * (s - ai) for ai in a) >> 1
    q = n * (n - 1) // 2
    g = math.gcd(p, q)
    p //= g
    q //= g
    print(p * pow(q, -1, MOD) % MOD)
