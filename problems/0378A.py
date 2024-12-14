# ruff: noqa: E731, E741
a, b = map(int, input().split())
x = y = z = 0
for d in range(1, 7):
    da = abs(d - a)
    db = abs(d - b)
    x += da < db
    y += da == db
    z += da > db
print(x, y, z)
