# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    print(1, *range(n, 1, -1))
