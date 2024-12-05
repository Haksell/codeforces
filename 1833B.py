# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = iter(sorted(map(int, input().split())))
    res = [-1] * n
    for i in sorted(range(n), key=a.__getitem__):
        res[i] = next(b)
    print(*res)
