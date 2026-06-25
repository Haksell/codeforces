# ruff: noqa: E731, E741
from collections import Counter
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(left, right):
    if left[-1] != right[0]:
        return len(left) * len(right)
    x = right[0]
    lc = left.count(x)
    rc = right.count(x)
    return len(left) * len(right) - lc * rc


def g(n, a, counter):
    ans = 0
    cleft = Counter()
    for i in range(1, n):
        left = a[i - 1]
        cleft[left] += 1
        right = a[i]
        cl = cleft[left]
        cr = counter[right] - cleft[right]
        x = i * (n - i) - (cl * cr if left == right else 0)
        # print(i, n - i, cl, cr, x)
        ans = max(ans, x)
    return ans


for _ in rir():
    n = ir()
    h = n >> 1
    a = sorted(lmir())
    counter = Counter(a)
    # print(a)
    if len(counter) == 1:
        print(n // 2)
    else:
        print(g(n, a, counter))
    # print()
