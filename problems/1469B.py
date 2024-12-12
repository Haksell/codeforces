# ruff: noqa: E731, E741
from itertools import accumulate

for _ in range(int(input())):
    n = int(input())
    r = map(int, input().split())
    m = int(input())
    b = map(int, input().split())
    print(max(accumulate(r, initial=0)) + max(accumulate(b, initial=0)))
