# ruff: noqa: E731, E741
from itertools import accumulate


def f(a):
    s = sum(a)
    if s % 3 != 0:
        return 0
    acc = list(accumulate(a[:-1]))
    one_third = s // 3
    two_third = one_third << 1
    res = 0
    current = 0
    for n in acc:
        if n == two_third:
            res += current
        if n == one_third:
            current += 1
    return res


n = int(input())
a = list(map(int, input().split()))
print(f(a))
