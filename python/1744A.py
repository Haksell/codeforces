# ruff: noqa: E731, E741
from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    d = defaultdict(list)
    for i, c in enumerate(a):
        d[c].append(i)
    for c, l in d.items():
        x = {s[i] for i in l}
        if len(x) > 1:
            print("NO")
            break
    else:
        print("YES")
