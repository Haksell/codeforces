# ruff: noqa: E731, E741
import sys


def operation(a):
    maxi = max(a)
    return [maxi - ai for ai in a]


for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    for _ in range(1 if k & 1 else 2):
        a = operation(a)
    print(*a)
