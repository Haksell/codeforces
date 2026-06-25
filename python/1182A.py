# ruff: noqa: E731, E741
n = int(input())
print(0 if n & 1 else 1 << (n >> 1))
