# ruff: noqa: E731, E741
from itertools import accumulate

for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    a = list(accumulate(h))
    print("YES" if all(x >= i * (i + 1) // 2 for i, x in enumerate(a)) else "NO")
