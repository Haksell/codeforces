# ruff: noqa: E731, E741
from math import inf


def longest(l):
    last = -inf
    res = cur = 0
    count = []
    for i, n in enumerate(l):
        if n > last:
            cur += 1
            if cur > res:
                res = cur
                count = [i]
            elif cur == res:
                count.append(i)
        else:
            cur = 1
        last = n
    return res, count


def g(l):
    (lg1, cnt1), (lg2, cnt2) = longest(l), longest(l[::-1])
    cnt2 = [len(l) - x - 1 for x in cnt2]
    return int(
        lg1 == lg2
        and lg1 % 2 == 1
        and len(cnt1) == 1
        and len(cnt2) == 1
        and cnt1 == cnt2
    )


n = int(input())
l = [int(x) - 1 for x in input().split()]
print(g(l))
