# ruff: noqa: E731, E741
x, y, z, s = sorted(list(map(int, input().split())))
print(s - x, s - y, s - z)
