# ruff: noqa: E731, E741
from collections import Counter
from itertools import count
from random import randint
import sys

cin = sys.stdin
read = cin.readline
cout = sys.stdout
write = cout.write
rir = lambda: range(int(read()))
ir = lambda: int(read())
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(n, k, lst):
    c = Counter(lst)
    a = max(c)
    b = next(i for i in count() if i not in c)

    for _ in range(k):
        new = a + b + 1 >> 1
        a = max(a, new)
        if new == b:
            b = next(i for i in count(b + 1) if i not in c)
        c[new] += 1

    return len(c)


def g(n, k, lst):
    c = Counter(lst)
    a = max(c)
    b = next(i for i in count() if i not in c)
    if a + 1 == b:
        return len(set(lst)) + k

    if k > 0:
        new = a + b + 1 >> 1
        c[new] += 1

    return len(c)


if 1:
    for _ in rir():
        n, k = mir()
        lst = lmir()
        print(g(n, k, lst))
else:
    n = 100
    k = 1000
    for _ in range(100):
        lst = [randint(0, 100) for _ in range(n)]
        assert f(n, k, lst) == g(n, k, lst), lst
