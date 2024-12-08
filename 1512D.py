# ruff: noqa: E731, E741
from heapq import nlargest


def yolo(a, m):
    a = a.copy()
    a.remove(m)
    s = sum(a) - m
    if s in a:
        a.remove(s)
        return a


def solve(a):
    m1, m2 = nlargest(2, a)
    return yolo(a, m1) or yolo(a, m2)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(a)
    print(*(ans or [-1]))
