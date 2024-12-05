# ruff: noqa: E731, E741
n, m = map(int, input().split())
print("Akshat" if min(n, m) & 1 else "Malvika")
