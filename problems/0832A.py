# ruff: noqa: E731, E741
n, k = map(int, input().split())
print("YES" if n // k & 1 else "NO")
