# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = n
    i = 0
    while i < res:
        m = max(a)
        mi = a.index(m)
        res = min(res, i + mi)
        a.remove(m)
        i += 1
    print(res)
