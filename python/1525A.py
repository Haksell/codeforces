# ruff: noqa: E731, E741
from math import gcd

for _ in range(int(input())):
    k = int(input())
    print(100 // gcd(k, 100 - k))
