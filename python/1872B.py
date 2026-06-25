# ruff: noqa: E731, E741
import sys

for _ in range(int(input())):
    res = sys.maxsize
    for i in range(int(input())):
        d, s = map(int, input().split())
        res = min(res, d + (s - 1 >> 1))
    print(res)
