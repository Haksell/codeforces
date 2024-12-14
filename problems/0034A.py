# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
i = min(range(n), key=lambda i: abs(a[i] - a[(i + 1) % n]))
print(i + 1, (i + 1) % n + 1)
