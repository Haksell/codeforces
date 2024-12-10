# ruff: noqa: E731, E741
from math import isqrt


def is_prime(n):
    return n >= 2 and all(n % i for i in range(2, isqrt(n) + 1))


for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print("FastestFinger")
    elif n == 2:
        print("Ashishgup")
    elif n & (n - 1) == 0:
        print("FastestFinger")
    elif n & 1 == 0 and is_prime(n >> 1):
        print("FastestFinger")
    else:
        print("Ashishgup")
