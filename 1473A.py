# ruff: noqa: E731, E741
from heapq import nsmallest

for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    min1, min2 = nsmallest(2, a)
    print("YES" if max(a) <= d or min1 + min2 <= d else "NO")
