# ruff: noqa: E731, E741
from math import factorial


def choose(n, k):
    return factorial(n) // factorial(k) // factorial(n - k) if 0 <= k <= n else 0


s1 = input()
s2 = input()
n1 = len(s1) - (s1.count("-") << 1)
n2 = s2.count("+") - s2.count("-")
d = abs(n1 - n2)
q = s2.count("?")
print(choose(q, q - d >> 1) / 2**q)
