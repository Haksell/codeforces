# ruff: noqa: E731, E741
from math import inf


def is_sorted(a):
    last = -inf
    for x in a:
        if x < last:
            return False
        last = x
    return True


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(
        0
        if is_sorted(a)
        else 1
        if a[0] == 1 or a[-1] == n
        else 3
        if a[0] == n and a[-1] == 1
        else 2
    )
