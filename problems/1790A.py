# ruff: noqa: E731, E741
from itertools import zip_longest

PI = "3141592653589793238462643383279"
for _ in range(int(input())):
    s = input()
    print(next(i for i, (c, p) in enumerate(zip_longest(PI, s)) if c != p))
