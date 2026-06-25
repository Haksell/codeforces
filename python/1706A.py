# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) - 1 for i in input().split()]
    a = [min(i, m - i - 1) for i in a]
    s = ["B"] * m
    for i, v in Counter(a).items():
        if v >= 2:
            s[i] = s[~i] = "A"
        elif v == 1:
            s[i] = "A"
    print("".join(s))
