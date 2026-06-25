# ruff: noqa: E731, E741
from collections import Counter


def solve(a, x):
    prev = 0
    below = 0
    for k, v in sorted(Counter(a).items()):
        water = (k - prev) * below
        if water > x:
            break
        x -= water
        below += v
        prev = k
    return prev + (x // below)


for _ in range(int(input())):
    n, x = map(int, input().split())
    a = sorted(map(int, input().split()))
    print(solve(a, x))
