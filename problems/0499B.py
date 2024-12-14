# ruff: noqa: E731, E741
n, m = map(int, input().split())
d = dict()
for _ in range(m):
    a, b = input().split()
    d[a] = a if len(a) <= len(b) else b
print(*map(d.__getitem__, input().split()))
