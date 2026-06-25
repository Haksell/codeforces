# ruff: noqa: E731, E741
a1, a2 = map(int, input().split())
print(max(0, a1 + a2 - 2 - (a1 % 3 == a2 % 3)))
