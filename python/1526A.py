# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    res = [None] * (2 * n)
    for i in range(n):
        res[2 * i] = a[i]
        res[2 * i + 1] = a[~i]
    print(*res)
