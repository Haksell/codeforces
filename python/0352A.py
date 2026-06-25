# ruff: noqa: E731, E741
n = int(input())
a = list(map(int, input().split()))
f = a.count(5)
print(-1 if f == n else 0 if f < 9 else f // 9 * 9 * "5" + (n - f) * "0")
