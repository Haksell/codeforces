# ruff: noqa: E731, E741
from itertools import accumulate


def smart(a):
    if a[0] <= 0 or a[-1] <= 0:
        return False
    acc = list(accumulate(a))
    if 0 in acc:
        return False
    y = sum(a)
    minsofar = 0
    for i, cursum in enumerate(acc):
        if cursum - minsofar >= y and (minsofar != 0 or i != len(a) - 1):
            return False
        minsofar = min(minsofar, cursum)
    return True


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if smart(a) else "NO")
