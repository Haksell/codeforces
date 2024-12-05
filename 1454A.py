# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    print(n, *range(1, n))
