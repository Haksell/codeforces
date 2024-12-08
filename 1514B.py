# ruff: noqa: E731, E741
MOD = 1_000_000_007
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(pow(n, k, MOD))
