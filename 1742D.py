# ruff: noqa: E731, E741
import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    last_occ = [-1] * (max(a) + 1)
    for i, ai in enumerate(a):
        last_occ[ai] = i
    res = -1
    for i, oi in enumerate(last_occ):
        if oi != -1:
            for j in range(1, i + 1):
                if last_occ[j] != -1 and math.gcd(i, j) == 1:
                    res = max(res, oi + last_occ[j] + 2)
    print(res)
