# ruff: noqa: E731, E741
from bisect import bisect_right

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    b = sorted(map(int, input().split()))
    c = map(int, input().split())
    print(sum(bisect_right(b, k - x) for x in c))
