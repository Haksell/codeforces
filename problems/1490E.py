# ruff: noqa: E731, E741
from heapq import nlargest
from itertools import accumulate


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sorted(a)
    c = list(accumulate(s))
    z = 1
    for i in range(n - 1):
        if c[i] >= s[i + 1]:
            z += 1
        else:
            z = 1
    x = nlargest(z, [(n, i) for i, n in enumerate(a)])
    print(z)
    print(*sorted(i + 1 for _, i in x))
