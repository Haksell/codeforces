# ruff: noqa: E731, E741
n, k = map(int, input().split())
h = list(map(int, input().split()))

minsum = s = sum(h[:k])
minidx = 1
for i in range(n - k):
    s += h[i + k] - h[i]
    if s < minsum:
        minsum = s
        minidx = i + 2
print(minidx)
