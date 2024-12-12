# ruff: noqa: E731, E741
n, s = map(int, input().split())
print(s // n + (s % n != 0))
