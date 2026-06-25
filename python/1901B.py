# ruff: noqa: E731, E741
from itertools import chain, islice


for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    c_next = chain(islice(c, 1, None), [0])
    print(sum(max(a - b, 0) for a, b in zip(c, c_next)) - (c[0] != 0))
