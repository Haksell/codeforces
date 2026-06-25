# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    i = n - 1 >> 1
    median = a[i]
    res = 0
    while i < n and a[i] == median:
        res += 1
        i += 1
    print(res)
