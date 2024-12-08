# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    argsort = sorted(range(n), key=a.__getitem__)
    a = [a[i] for i in argsort]
    b = [b[i] for i in argsort]
    for ai, bi in zip(a, b):
        if ai > k:
            break
        k += bi
    print(k)
