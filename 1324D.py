# ruff: noqa: E731, E741
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = sorted([ai - bi for ai, bi in zip(a, b)])
print(sum(n - bisect_left(d, -x + 1) - (x > 0) for x in d) >> 1)
