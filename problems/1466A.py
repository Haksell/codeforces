# ruff: noqa: E731, E741
from itertools import combinations

for _ in range(int(input())):
    n = int(input())
    xs = list(map(int, input().split()))
    s = {abs(x1 - x2) for x1, x2 in combinations(xs, 2)}
    print(len(s))
