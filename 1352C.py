# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(k + (k - 1) // (n - 1))
