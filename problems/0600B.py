# ruff: noqa: E731, E741
from bisect import bisect_right

input()
a = sorted(map(int, input().split()))
print(*[bisect_right(a, int(n)) for n in input().split()])
