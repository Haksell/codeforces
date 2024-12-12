# ruff: noqa: E731, E741
from collections import Counter
from itertools import count

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    b = []
    for i in count():
        if c[i] >= 1:
            b.append(i)
            c[i] -= 1
        else:
            break
    b.extend([k for k, v in c.items() for _ in range(v)])
    print(*b)
