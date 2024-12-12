# ruff: noqa: E731, E741
from collections import Counter
from math import isqrt


n = int(input())
a = list(map(int, input().split()))
x = max(a)
c = Counter(a)
isqrtx = isqrt(x)
for i in range(1, isqrtx + 1):
    if x % i == 0:
        c[i] -= 1
        if i * i != x:
            c[x // i] -= 1
print(x, max(k for k, v in c.items() if v != 0))
