# ruff: noqa: E731, E741
from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = [k for k, _ in groupby(a)]
    print("NO" if any(x > y < z for x, y, z in zip(a, a[1:], a[2:])) else "YES")
