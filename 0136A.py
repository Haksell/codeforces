# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
print(*sorted(range(1, n + 1), key=lambda i: a[i - 1]))
