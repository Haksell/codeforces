# ruff: noqa: E731, E741
"""
6: 3 2 1
7: !
8: 5 2 1
9: 5 3 1
10: 7 2 1
11: 7 3 1
12: 9 2 1
13:
"""

for _ in range(int(input())):
    n = int(input())
    h = n >> 1
    if n & 1 == 0:
        print(n - 3, 2, 1)
    elif n & 3 == 1:
        print(h + 1, h - 1, 1)
    else:
        print(h + 2, h - 2, 1)
