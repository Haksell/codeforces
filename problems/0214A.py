# ruff: noqa: E731, E741
n, m = map(int, input().split())
res = 0
for a in range(32):
    for b in range(32):
        res += a * a + b == n and a + b * b == m
print(res)
