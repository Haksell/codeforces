# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))
    res = 0
    lo, hi = 0, n - 1
    left = right = 0
    while lo <= hi:
        if left <= right:
            left += w[lo]
            lo += 1
        else:
            right += w[hi]
            hi -= 1
        if left == right:
            res = max(res, n + lo - hi - 1)
    print(res)
