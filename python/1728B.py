# ruff: noqa: E731, E741
"""
4: 2 1 3 4
5: 1 3 2 4 5
6: 4 3 2 1 5 6
8: 6 5 4 3 2 1 7 8
"""

for _ in range(int(input())):
    n = int(input())
    if n & 1:
        print(1, *range(n - 2, 1, -1), n - 1, n)
    else:
        print(*range(n - 2, 0, -1), n - 1, n)
