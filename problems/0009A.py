# ruff: noqa: E731, E741
from math import gcd

y, w = map(int, input().split())
n = 7 - max(y, w)
g = gcd(n, 6)
print(f"{n//g}/{6//g}")
