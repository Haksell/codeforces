# ruff: noqa: E731, E741
from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()), key=lambda n: n & 1)
    print(sum(gcd(a[i], a[j] << 1) > 1 for i in range(n) for j in range(i + 1, n)))
