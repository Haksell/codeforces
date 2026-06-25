# ruff: noqa: E731, E741
from itertools import accumulate


for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    print(*accumulate(x, initial=sum(x) + 1))
