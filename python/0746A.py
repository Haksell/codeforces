# ruff: noqa: E731, E741
a = int(input())
b = int(input())
c = int(input())
print(7 * min(a, b >> 1, c >> 2))
