# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    res = [0] * n
    for i, ai in enumerate(a[: n // 2]):
        res[-2 * i - 2] = ai
    for i, ai in enumerate(a[n // 2 :][::-1]):
        res[-2 * i - 1] = ai
    print(*res)
