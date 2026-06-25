# ruff: noqa: E731, E741
from bisect import bisect_left, bisect_right

for _ in range(int(input())):
    _, l, r = map(int, input().split())
    a = sorted(map(int, input().split()))
    ans = 0
    for i, x in enumerate(a):
        li = max(bisect_left(a, l - x), i + 1)
        ri = bisect_right(a, r - x) - 1
        if ri >= li:
            ans += ri - li + 1
    print(ans)
