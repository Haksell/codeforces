# ruff: noqa: E731, E741
from cmath import inf
from itertools import accumulate


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ml = list(accumulate(a, min, initial=inf))
    mr = list(accumulate(a[::-1], min, initial=inf))[::-1]
    for i, ai in enumerate(a):
        if ai > ml[i] and ai > mr[i + 1]:
            li = min(range(i), key=a.__getitem__)
            ri = min(range(i + 1, n), key=a.__getitem__)
            print("YES")
            print(li + 1, i + 1, ri + 1)
            break
    else:
        print("NO")
