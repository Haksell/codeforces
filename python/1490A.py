# ruff: noqa: E731, E741
from math import ceil, log2


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    z = 0
    for i in range(n - 1):
        x = max(0, ceil(log2(a[i + 1] / a[i])) - 1)
        z += x
    print(z)
