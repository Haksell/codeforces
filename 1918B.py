# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*range(1, n + 1))
    idx = [-1] * n
    for i, ai in enumerate(a):
        idx[ai - 1] = i
    print(*[b[i] for i in idx])
