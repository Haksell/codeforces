# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    l = list(range(1, n + 1))
    for i in range(0, n - 1, 2):
        l[~i], l[~i - 1] = l[~i - 1], l[~i]
    print(*l)
