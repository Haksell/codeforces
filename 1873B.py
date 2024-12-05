# ruff: noqa: E731, E741
from math import prod


for _ in range(int(input())):
    input()
    a = sorted(map(int, input().split()))
    print(-~a[0] * prod(a[1:]))
