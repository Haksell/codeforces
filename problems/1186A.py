# ruff: noqa: E731, E741
n, m, k = map(int, input().split())
print("Yes" if m >= n and k >= n else "No")
