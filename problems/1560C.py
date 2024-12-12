# ruff: noqa: E731, E741
from math import isqrt

for _ in range(int(input())):
    k = int(input())
    a = isqrt(k - 1)
    b = k - a * a - 1
    if b <= a:
        print(b + 1, a + 1)
    else:
        print(a + 1, a + a - b + 1)
