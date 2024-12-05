# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for ai in a:
        res += 1
        if ai == res:
            res += 1
    print(res)
