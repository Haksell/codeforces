# ruff: noqa: E731, E741
from math import inf

for _ in range(int(input())):
    s = input()
    l1 = l2 = l3 = None
    res = inf
    for i, c in enumerate(s):
        if c == "1":
            l1 = i
        elif c == "2":
            l2 = i
        else:  # c == "3"
            l3 = i
        if l1 is not None and l2 is not None and l3 is not None:
            res = min(res, max(l1, l2, l3) - min(l1, l2, l3) + 1)
    print(0 if res == inf else res)
