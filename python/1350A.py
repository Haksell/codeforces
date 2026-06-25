# ruff: noqa: E731, E741
from math import isqrt

size = 10**6 + 1
smallest_factor = list(range(size))
smallest_factor[0] = smallest_factor[1] = None
for i in range(2, isqrt(size) + 1):
    if smallest_factor[i] == i:
        for j in range(i * i, size, i):
            if smallest_factor[j] == j:
                smallest_factor[j] = i

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(n + smallest_factor[n] + 2 * (k - 1))
