# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(1 if k >= n - 1 else n)
