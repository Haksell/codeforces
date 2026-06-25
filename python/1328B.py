# ruff: noqa: E731, E741
"""
x=n(n+1)/2
2x=nn+n
2x=(n+1/2)^2-1/4
sqrt(2x+1/4)=n+1/2
sqrt(2x+1/4)-1/2=n
"""

from math import sqrt


def triangle(k):
    return k * (k + 1) >> 1


def inverse_triangle(k):
    return int(sqrt(k + k + 0.25) - 0.5)


for _ in range(int(input())):
    n, k = map(int, input().split())
    k -= 1
    i = inverse_triangle(k)
    k -= triangle(i)
    s = ["a"] * n
    s[-i - 2] = "b"
    s[-k - 1] = "b"
    print("".join(s))
