# ruff: noqa: E731, E741
from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    s = input()
    print("Yes" if s.count("1") > sum(k == "0" for k, _ in groupby(s)) else "No")
