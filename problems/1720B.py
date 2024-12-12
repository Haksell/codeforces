# ruff: noqa: E731, E741
from heapq import nlargest, nsmallest

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(nlargest(2, a)) - sum(nsmallest(2, a)))
