# ruff: noqa: E731, E741
from itertools import count
from math import gcd


def find_x(left, right):
    for i in count(right + 1):
        if gcd(left, i) == 1 == gcd(right, i):
            return i


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mini = min(range(n), key=a.__getitem__)
    ans = []
    for i in range(n - 1):
        left = a[i]
        right = a[i + 1]
        if gcd(left, right) == 1:
            continue
        elif left <= right:
            x = left
            y = left + 1
        else:
            x = right + 1 if i == 0 else find_x(a[i - 1], right)
            y = right
        a[i] = x
        a[i + 1] = y
        ans.append((i + 1, i + 2, x, y))
    print(len(ans))
    for i, j, x, y in ans:
        print(i, j, x, y)
