# ruff: noqa: E731, E741
from heapq import nlargest, nsmallest

for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    min1, min2 = nsmallest(2, a)
    max1, max2 = nlargest(2, a)
    print(max(min1 * min2, max1 * max2))
