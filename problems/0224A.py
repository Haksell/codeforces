# ruff: noqa: E731, E741
from math import sqrt

a, b, c = map(int, input().split())
x = sqrt(a * b / c)
y = sqrt(b * c / a)
z = sqrt(c * a / b)
print(round(4 * (x + y + z)))
