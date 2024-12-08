# ruff: noqa: E731, E741
from itertools import accumulate

for _ in range(int(input())):
    _, x = map(int, input().split())
    w = list(map(int, input().split()))
    if sum(w) == x:
        print("NO")
    else:
        print("YES")
        acc = list(accumulate(w))
        if x in acc:
            i = acc.index(x)
            w[i], w[i + 1] = w[i + 1], w[i]
        print(*w)
