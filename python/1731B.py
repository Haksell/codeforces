# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MOD = 1_000_000_007
for _ in rir():
    n = ir()
    ans = n * (n - 1) * (2 * n - 1) // 3 + n * (n - 1) // 2 + n * n
    print(2022 * ans % MOD)
