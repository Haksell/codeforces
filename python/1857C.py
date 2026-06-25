# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    for k, v in sorted(Counter(b).items()):
        while v:
            n -= 1
            v -= n
            a.append(k)
    a.append(a[-1])
    print(*a)
