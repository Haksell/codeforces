# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    if n & 1:
        print(*range(1, n + 1 >> 1), *range(n, n >> 1, -1))
    else:
        print(-1)
