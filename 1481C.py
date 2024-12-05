# ruff: noqa: E731, E741
from collections import defaultdict


def f():
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = defaultdict(list)
    for i, (ax, bx) in enumerate(zip(a, b)):
        if ax != bx:
            d[bx].append(i)

    e = {x: i for i, x in enumerate(b)}
    lst = []
    s = set()
    for x in reversed(c):
        if x in d:
            y = d[x].pop()
            if not d[x]:
                del d[x]
        elif s:
            y = next(iter(s))
        else:
            try:
                y = e[x]
            except KeyError:
                print("NO")
                return
        lst.append(y)
        s.add(y)

    for i, y in enumerate(reversed(lst)):
        a[y] = c[i]
    if a != b:
        print("NO")
    else:
        print("YES")
        print(*(x + 1 for x in reversed(lst)))


for _ in range(int(input())):
    f()
