# ruff: noqa: E731, E741
from itertools import chain


def consecutive(s, c):
    return next(i for i, x in enumerate(chain(s, [object()])) if x != c)


for _ in range(int(input())):
    n = int(input())
    s = input()
    if len(set(s)) == 1 or s.rindex("0") < s.index("1"):
        print(s)
    else:
        z = consecutive(s, "0")
        o = consecutive(reversed(s), "1")
        print("0" * (z + 1) + "1" * o)
