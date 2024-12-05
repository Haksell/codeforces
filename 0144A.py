# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
max_idx = max(range(n), key=lambda i: (a[i], -i))
min_idx = min(range(n), key=lambda i: (a[i], -i))
res = max_idx + (n - 1 - min_idx) - (max_idx > min_idx)
print(res)
