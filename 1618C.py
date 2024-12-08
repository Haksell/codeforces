# ruff: noqa: E731, E741
from math import gcd


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g0 = gcd(*a[0::2])
    g1 = gcd(*a[1::2])
    if all(a0 % g1 for a0 in a[0::2]):
        print(g1)
    elif all(a1 % g0 for a1 in a[1::2]):
        print(g0)
    else:
        print(0)
