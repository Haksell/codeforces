# ruff: noqa: E731, E741
from math import gcd


def solve(l, r):
    for i in range(l, r - 1):
        for j in range(i + 1, r):
            if gcd(i, j) != 1:
                break
            for k in range(j + 1, r + 1):
                if gcd(j, k) == 1 and gcd(i, k) != 1:
                    return (i, j, k)
    return (-1,)


print(*solve(*map(int, input().split())))
