# ruff: noqa: E731, E741
from heapq import nlargest, nsmallest

n = int(input())
a = list(map(int, input().split()))
max1, max2 = nlargest(2, a)
min1, min2 = nsmallest(2, a)
print(min(max1 - min2, max2 - min1))
