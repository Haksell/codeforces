# ruff: noqa: E731, E741
n, k = map(int, input().split())
if 2 * k <= n + 1:
    print(2 * k - 1)
else:
    print(2 * (k - (n + 1) // 2))
