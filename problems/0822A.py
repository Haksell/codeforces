# ruff: noqa: E731, E741
from math import factorial

a, b = map(int, input().split())
print(factorial(min(a, b)))
