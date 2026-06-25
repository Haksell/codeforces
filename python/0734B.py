# ruff: noqa: E731, E741
k2, k3, k5, k6 = map(int, input().split())
a = min(k2, k5, k6)
b = min(k2 - a, k3)
print(a * 256 + b * 32)
