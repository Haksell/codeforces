# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, x, m = map(int, input().split())
    mini = maxi = x
    for _ in range(m):
        l, r = map(int, input().split())
        if l <= mini <= r:
            mini = l
        if l <= maxi <= r:
            maxi = r
    print(maxi - mini + 1)
