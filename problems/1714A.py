# ruff: noqa: E731, E741
from math import inf

for _ in range(int(input())):
    n, H, M = map(int, input().split())
    T = 60 * H + M
    res = inf
    for _ in range(n):
        h, m = map(int, input().split())
        t = 60 * h + m
        res = min(res, (t - T) % 1440)
    print(*divmod(res, 60))
