# ruff: noqa: E731, E741
from math import factorial

n = int(input())
print(factorial(2 * n - 2) // factorial(n - 1) ** 2)
