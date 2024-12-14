# ruff: noqa: E731, E741
n, d = map(int, input().split())
t = list(map(int, input().split()))
s = sum(t)
tot = s + 10 * (n - 1)
print(-1 if tot > d else (d - s) // 5)
