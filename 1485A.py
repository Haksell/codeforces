# ruff: noqa: E731, E741
from itertools import count


def f(a, b):
    q = [(a, b)]
    for i in count():
        nq = []
        for a, b in q:
            if a == 0:
                return i
            nq.append((a // b, b))
            nq.append((a, b + 1))
        q = nq


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(f(a, b))
