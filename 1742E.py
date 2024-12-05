# ruff: noqa: E731, E741
from bisect import bisect
from itertools import accumulate


def solve(cumsum, cummax, ki):
    idx = bisect(cummax, ki)
    return cumsum[idx - 1]


for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    cumsum = list(accumulate(a, initial=0))
    cummax = list(accumulate(a, max, initial=0))
    k = list(map(int, input().split()))
    print(*[solve(cumsum, cummax, ki) for ki in k])
